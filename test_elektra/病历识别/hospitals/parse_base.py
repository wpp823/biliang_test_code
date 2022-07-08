import re
import typing

import arrow
from flashtext import KeywordProcessor
from pydantic.fields import ModelField

from hospital_map import hospital_map, DEFAULT_HOSTPITAL_CLASS_NAME
from modal import MedicalRecord


class ReZoo:
    RE_CHINESE = re.compile("[\u4e00-\u9fa5]+")  # 中文正则表达式
    RE_GENDER = re.compile("^性别[：\s:]*([男|女])")
    RE_NUM = re.compile('\d+')

    RE_STD_DATE = re.compile('^[12][\d]{3}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}(:[\d]{2})?$')
    RE_STD_DAY = re.compile('[12][\d]{3}-[\d]{2}-[\d]{2}')

    Re_Num_Char = re.compile(r'[0-9a-zA-Z]+')
    RE_BLANK = re.compile(r"\s+")


def DBC2SBC(ustring):
    ' 全角转半角 ”'
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
            rstring += uchar
            continue
        rstring += chr(inside_code)
    return rstring


def SBC2DBC(ustring):
    ' 半角转全角 ”'
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
        inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring


class ParseBase:
    '''
    所以识别类的基类，一些基础识别方法定义。
    '''

    def __init__(self, log, recogn_result):
        '''
        
        :param log:     [log]
        :param recogn_result:  [list(dict)]ocr识别后的结果。
        '''
        self._log = log
        self._recogn_result = recogn_result

        self._all_recogn_str = None  # 忽略位置信息，将所有内容组成一个字符串。

    @property
    def recogn_str(self):
        '''
        所有识别出来的内容连接成字符串。
        :return:
        '''

        if not self._all_recogn_str:
            recogn_str_list = [item["text"] for item in self._recogn_result]
            self._all_recogn_str = "".join(recogn_str_list)

        return self._all_recogn_str

    def _get_medica_record_obj(self, medica_record_class):
        '''
        获取病历对象。
        :param medica_record_class:     [class]是病历类。
        :return:    [object]        medica_record_class的实例。
        '''

        med_dict = {}

        for i in dir(medica_record_class):
            attr_name = getattr(medica_record_class, i)
            if isinstance(attr_name, dict):
                for k, v in attr_name.items():
                    if isinstance(v, ModelField):
                        func_name = "parse_{}".format(k)
                        try:
                            ocr_func = getattr(self, func_name)
                            ocr_result = ocr_func(self._recogn_result)

                            med_dict[k] = ocr_result
                        except:
                            self._log.error("[{}.{}][fields:{}]".format(medica_record_class.__name__, func_name, k))

        # 修正姓名错误 张三性别男 李四性别:女 @202107151018
        if med_dict.get('name') and med_dict['name'].find("性别") > -1:
            _part_list = med_dict['name'].split('性别')

            # med_dict['name'] = _part_list[0]
            # 会出现 空格, 、 等非中文字符
            med_dict['name'] = "".join(ReZoo.RE_CHINESE.findall(_part_list[0]))

            if not med_dict.get('gender'):
                gender_result = ReZoo.RE_GENDER.match('性别' + _part_list[1])
                if gender_result:
                    med_dict['gender'] = gender_result.group(1)

        # 修正姓名错误 单字 @202107151018
        if med_dict.get('name') and len(med_dict['name']) == 1:
            med_dict['name'] = None

        # 修正医生名可能的错误
        if med_dict.get('doctor_name'):
            med_dict['doctor_name'] = "".join(ReZoo.RE_CHINESE.findall(med_dict['doctor_name']))
            if len(med_dict['doctor_name']) <= 1:
                med_dict['doctor_name'] = None

        med_obj = medica_record_class(**med_dict)

        self._log.info("[{}.get_medica_record_obj][{}]".format(medica_record_class.__name__, med_obj.json(ensure_ascii=False)))

        return med_obj

    def _parse_simple_regex_str(self, recogn_str, regex_template, group=0, match=True):
        '''
        从识别结果中提取正则表达式的匹配中的文字
        :param recogn_str:          [str]一个字符串。
        :param regex_template:      [str]正则表达式
        :param group:               [int]0代表匹配到全部，>0 代表取指定的组。
        :param match:               [bool]true,代表使用match函数，false代表使用search函数
        '''

        result_txt = None

        match_result = None
        if match:
            match_result = re.match(regex_template, recogn_str)
        else:
            match_result = re.search(regex_template, recogn_str)
        if match_result:
            result_txt = match_result.group(group)

        return result_txt

    def _parse_simple_regex(self, recogn_result, regex_template, group=0, match=True):
        '''
        从识别结果中提取正则表达式的匹配中的文字 。
        :param recogn_result:       [dict]从paddleOCR中返回的值。
        :param regex_template:      [str]正则表达式
        :param group:               [int]0代表匹配到全部，>0 代表取指定的组。
        :param match:               [bool]true,代表使用match函数，false代表使用search函数
        :return:
        '''
        re_obj = re.compile(regex_template)
        for rec_item in recogn_result:
            item_text = rec_item["text"]

            match_result = None
            if match:
                match_result = re_obj.match(item_text)
            else:
                match_result = re_obj.search(item_text)
            if match_result:
                result_txt = match_result.group(group)
                self._log.info(
                    "[parse_simple_ok][template:{}, result:{}, src:{}]".format(regex_template, result_txt, item_text))
                return result_txt

        self._log.warning("[parse_simple_failed][template:{}]".format(regex_template))

        return None

    def _parse_complex_middle(self, recogn_result, begin_reg_templ, end_reg_templ, include_end: bool = False) -> typing.List[str]:
        '''
        提取两个正则表达式之间的所有数据，
        :param recogn_result:
        :param begin_regex_templ:     [regex]包含此数据，从此数据开始
        :param end_regex_templ:       [regex]不包括此数据。 到此数据结束。
        :return:
        '''

        base_stamp_index = 0
        history_text_list = []

        re_obj = re.compile(begin_reg_templ)  # 找到开始位置。
        for rec_item in recogn_result:
            item_text = rec_item["text"]

            match_result = re_obj.match(item_text)
            if match_result:
                history_text_list.append(item_text)
                break
            base_stamp_index += 1

        rec_len = len(recogn_result)

        if base_stamp_index == 0 or base_stamp_index >= rec_len - 1:
            self._log.warning("[__parse_complex_middle][no found begin][regex:{}]".format(begin_reg_templ))  # 没有发现开始。
            return history_text_list

        # 找结束表达式出现的地方
        for tmp_idx in range(base_stamp_index + 1, rec_len):
            tmp_text = recogn_result[tmp_idx]["text"]

            if re.search(end_reg_templ, tmp_text):  # 再找结束位置 。
                if include_end:
                    history_text_list.append(tmp_text)
                break

            history_text_list.append(tmp_text)

        if tmp_idx < rec_len - 1:
            # 由于 “：“ 出现的地方是在结束行之前，所以，是有效的。

            self._log.info(
                "[__parse_complex_middle][line_count:{}]".format(len(history_text_list)))

        else:
            history_str = recogn_result[base_stamp_index]["text"]
            self._log.warning(
                "[__parse_complex_middle][no found end][end_regex:{}][result:{}]".format(end_reg_templ, history_str))

        return history_text_list

    def _parse_complex_middle_v2(self, recogn_result, begin_reg_templ, end_reg_templ, include_end: bool = False,
                                 exclude_re_if_end_not_found: str = None,
                                 ) -> typing.List[str]:
        '''
        提取两个正则表达式之间的所有数据，
        :param recogn_result:
        :param begin_regex_templ:     [regex]包含此数据，从此数据开始
        :param end_regex_templ:       [regex]不包括此数据。 到此数据结束。
        :return:
        '''

        base_stamp_index = 0
        history_text_list = []
        _end_found = False

        re_obj = re.compile(begin_reg_templ)  # 找到开始位置。
        for rec_item in recogn_result:
            item_text = rec_item["text"]

            match_result = re_obj.match(item_text)
            if match_result:
                history_text_list.append(item_text)
                break
            base_stamp_index += 1

        rec_len = len(recogn_result)

        if base_stamp_index == 0 or base_stamp_index >= rec_len - 1:
            self._log.warning("[__parse_complex_middle][no found begin][regex:{}]".format(begin_reg_templ))  # 没有发现开始。
            return history_text_list

        # 找结束表达式出现的地方
        for tmp_idx in range(base_stamp_index + 1, rec_len):
            tmp_text = recogn_result[tmp_idx]["text"]

            if re.search(end_reg_templ, tmp_text):  # 再找结束位置 。
                _end_found = True
                if include_end:
                    history_text_list.append(tmp_text)
                break

            history_text_list.append(tmp_text)

        if tmp_idx < rec_len - 1:
            # 由于 “：“ 出现的地方是在结束行之前，所以，是有效的。

            self._log.info(
                "[__parse_complex_middle][line_count:{}]".format(len(history_text_list)))

        else:
            # 找不到结束标志
            history_str = recogn_result[base_stamp_index]["text"]
            self._log.warning(
                "[__parse_complex_middle][no found end][end_regex:{}][result:{}]".format(end_reg_templ, history_str))

            # 剔除无效的
            if exclude_re_if_end_not_found:
                re_exclude_obj = re.compile(exclude_re_if_end_not_found)

                for h_i, h_text in enumerate(history_text_list):
                    if h_i == 0:
                        continue

                    if re_exclude_obj.search(h_text) is not None:
                        return history_text_list[:h_i]

        return history_text_list

    def _parse_complex_after(self, recogn_result, begin_reg_templ, include_begin: bool = False) -> typing.Optional[str]:
        """
        提取begin_reg_templ后的第一个文本
        """

        base_stamp_index = 0
        history_text_list = []

        re_obj = re.compile(begin_reg_templ)  # 找到开始位置。
        for rec_item in recogn_result:
            item_text = rec_item["text"]

            match_result = re_obj.match(item_text)
            if match_result:
                history_text_list.append(item_text)
                break
            base_stamp_index += 1

        rec_len = len(recogn_result)

        if base_stamp_index == 0 or base_stamp_index >= rec_len - 1:
            self._log.warning("[__parse_complex_middle][no found begin][regex:{}]".format(begin_reg_templ))  # 没有发现开始。
            return None

        # 下一个文本
        tmp_text = recogn_result[base_stamp_index + 1]["text"]
        if not include_begin:
            return tmp_text

        return recogn_result[base_stamp_index]["text"] + tmp_text

    def parse_hospital_name(self, recogn_result):
        '''
        解析医院名称。这是标准方法。
        :param recogn_result:   []_recognition识别结果，结构如下：
                            {'confidence': 0.9973363280296326, 'text': '深圳市中医院',
                           'text_region': [[307, 277], [815, 240], [820, 300], [311, 337]]},
        :return:    str
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template=".+医院.*")

    def parse_hospital_alisa_name(self, recogn_result):
        '''
        获取医院的别名
        :param recogn_result:
        :return:    str
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template=".+医学院.*")

    def parse_hospital_english_name(self, recogn_result):
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template=".+HOSPITAL.*")


def get_hospital_schedular_class_name(log, recogn_result, ocr_hostpital_name=None) -> str:
    '''
    使用多种方法获取医院名称或别名，获取医院的调度类名称。
    :param log:
    :param recogn_result:
    :param ocr_hostpital_name:  [str]医院的OCR名称。
    :return:    str
    '''

    base_parse = ParseBase(log=log, recogn_result=recogn_result)

    hostpital_name = ocr_hostpital_name

    if hostpital_name == None:
        hostpital_name = base_parse.parse_hospital_name(recogn_result=recogn_result)

    hostpital_class_name = hospital_map.get(hostpital_name, None)  # 先找到相应的医院解析类名。

    search_method = "ParseBase.parse_hospital_name"

    if not hostpital_class_name and not ocr_hostpital_name:  # 没有传OCR医院名称，这时要猜其医院名称。
        search_method = "ParseBase.parse_hospital_alisa_name"
        hostpital_name = base_parse.parse_hospital_alisa_name(recogn_result=recogn_result)
        hostpital_class_name = hospital_map.get(hostpital_name, None)  # 先找到相应的医院解析类名。

        # 中文未匹配成功进行英文匹配
        if not hostpital_class_name and not ocr_hostpital_name:
            search_method = "ParseBase.parse_hospital_english_name"
            hostpital_name = base_parse.parse_hospital_english_name(recogn_result=recogn_result)
            hostpital_class_name = hospital_map.get(hostpital_name, None)  # 先找到相应的医院解析类名。

        if not hostpital_class_name:  # 如果别名也没有猜到，就用全局名称匹配了。

            search_method = "all_text_search.flashtext"

            # 对医院与解析类的映射表进行键值反转。转在flashtext所需要的结构
            temp_hospital_dict = {}

            for k, v in hospital_map.items():
                tmp_hosp_name_list = temp_hospital_dict.get(v, [])
                tmp_hosp_name_list.append(k)
                temp_hospital_dict[v] = tmp_hosp_name_list

            # temp_hospital_dict = dict(zip(hospital_map.values(), hospital_map.keys()))

            keyword_processor = KeywordProcessor(case_sensitive=False)
            keyword_processor.set_non_word_boundaries([])

            keyword_processor.add_keywords_from_dict(temp_hospital_dict)

            # 提取对应的关键字所对应的值。
            found_vals = keyword_processor.extract_keywords(sentence=base_parse.recogn_str)

            if found_vals:
                hostpital_class_name = found_vals[0]

    if hostpital_class_name:
        log.info("[get_hospital_schedular_class_name_ok][method:{}][name:{}, class:{}]".format(search_method, hostpital_name, hostpital_class_name))
    else:
        hostpital_class_name = DEFAULT_HOSTPITAL_CLASS_NAME
        log.error("[get_hospital_schedular_class_name_ok][all_method_failed, and user default hospital_class:{}]".format(hostpital_class_name))

    return hostpital_class_name


class DefaultMedicaRecordParse(ParseBase):
    '''
    默认病历解析器
    '''

    def get_medica_record_obj(self) -> MedicalRecord:
        '''
        获取病历对象。
        :return:
        '''

        return self._get_medica_record_obj(MedicalRecord)

        # med_dict = {}
        #
        # for i in dir(SzszyyMedicaRecord):
        #     attr_name = getattr(SzszyyMedicaRecord, i)
        #     if isinstance(attr_name, dict):
        #         for k, v in attr_name.items():
        #             if isinstance(v, ModelField):
        #                 ocr_func = getattr(self, "parse_{}".format(k))
        #                 ocr_result = ocr_func(self._recogn_result)
        #
        #                 med_dict[k] = ocr_result
        #
        # med_obj = SzszyyMedicaRecord(**med_dict)
        # self._log.info("[FirstMedicaRecordParse.get_medica_record_obj][{}]".format(med_obj.json(ensure_ascii=False)))
        #
        # return med_obj

    def parse_name(self, recogn_result):
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^姓名[：\s:]*(.+)$", group=1)

    def parse_gender(self, recogn_result):
        '''
        性别
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^性别[：\s:]*([男|女])", group=1)

    def parse_age(self, recogn_result):
        '''
        年龄
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="年龄[：\s:]*([0-9]+)岁", group=1, match=False)

    def parse_physical_examination(self, recogn_result):
        '''
        体检
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^体检[：\s:]*(.+)$", group=1)

    @classmethod
    def util_parse_date_num(cls, num_list: typing.List[int]) -> typing.Optional[arrow.Arrow]:
        """ """
        num_count = len(num_list)
        std_date = None
        num_str = "".join([str(x) for x in num_list])

        if num_count in {14, 12}:
            if num_count == 12:
                std_date = f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]} {num_str[8:10]}:{num_str[10:12]}:00"
            else:
                std_date = f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]} {num_str[8:10]}:{num_str[10:12]}:{num_str[12:14]}"

        elif 10 <= num_count < 14 and ReZoo.RE_STD_DAY.match(f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]}") is not None:
            # 补零
            if num_count == 13:
                # 在小时处补 0
                num_list.insert(8, 0)
                num_str = "".join([str(x) for x in num_list])
                std_date = f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]} {num_str[8:10]}:{num_str[10:12]}:{num_str[12:14]}"
            elif num_count in {10, 11}:
                # 数字分配到 时 分
                if num_count == 10:
                    std_date = f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]} 0{num_str[8:9]}:0{num_str[9:]}:00"
                else:
                    if 10 * num_list[9] + num_list[10] < 60:
                        std_date = f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]} 0{num_str[8:9]}:{num_str[9:11]}:00"
                    else:
                        std_date = f"{num_str[:4]}-{num_str[4:6]}-{num_str[6:8]} {num_str[8:10]}:0{num_str[9:10]}:00"

        if not std_date:
            return None

        if ReZoo.RE_STD_DATE.match(std_date) is not None:
            try:
                return arrow.get(std_date).replace(tzinfo="Asia/Shanghai")
            except Exception:
                return

        return None

    def parse_inquiry_at(self, recogn_result):
        '''
        就诊时间
        :param recogn_result:
        :return: 2021-02-02 10:02

        2021-08181 50
        2021-08-07 -15:33
        2021-06051 430
        2021-08-23 08:13
        2021-08-03 -15:47
        202108-171 1:15
        2021-08181 50
        '''
        at_str = self._parse_simple_regex(recogn_result=recogn_result, regex_template=r"^就诊时间[：\s:]*([\d\-\:：]+)$", group=1)
        if at_str:
            num_list = []
            for x in ReZoo.RE_NUM.findall(at_str):
                for num in x:
                    num_list.append(int(num))

            arrow_obj = DefaultMedicaRecordParse.util_parse_date_num(num_list=num_list)
            if arrow_obj:
                return arrow_obj.format("YYYY-MM-DD HH:mm")

        return None

    def parse_department_name(self, recogn_result):
        '''
        就诊科室
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^就诊科室[：\s:]*(.+)$", group=1)

    def parse_regist_no(self, recogn_result):
        '''
        就诊登记号
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template=r"^登记号[：\s:]*(\d+)$", group=1)

    def parse_patient_tells(self, recogn_result):
        '''
        主诉
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^主诉[：\s:]*(.+)$", group=1)

    def parse_medical_allergy(self, recogn_result):
        '''
        过敏史
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^过敏史[：\s:]*(.+)$", group=1)

    def parse_cmd(self, recogn_result):
        '''
        中医诊断
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^中医诊断[：\s:]*(.+)$", group=1)

    def parse_wmd(self, recogn_result):
        '''
        西医诊断
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^西医诊断[：\s:]*(.+)$", group=1)

    def parse_doctor_name(self, recogn_result):
        '''
        医生姓名，获取过程，是先找到“签字盖章”四个字，然后找其前一个和后两个解决出来的对象，根据这两个对象的长度来进行预判是否为名称。
        :param recogn_result:
        :return:
        '''
        base_stamp_index = 0

        re_obj = re.compile("^签字盖章")
        for rec_item in recogn_result:
            item_text = rec_item["text"]

            match_result = re_obj.match(item_text)
            if match_result:
                break
            base_stamp_index += 1

        doctor_name = None
        # 向前取一个对象。
        befor_text = recogn_result[base_stamp_index - 1]["text"]
        if len(befor_text) < 5:
            if not re.search(r"[\d,\+\-]+", befor_text):  # 名字小于5个字，且字符中没有数据和标点符号。
                doctor_name = befor_text

        rec_len = len(recogn_result)

        # 向后取2个对象
        for idx in range(1, 3):
            if not doctor_name and rec_len > base_stamp_index + idx:
                next_text = recogn_result[base_stamp_index + idx]["text"]
                if len(next_text) < 5:
                    if not re.search(r"[\d,\+\-]+", next_text):  # 名字小于5个字，且字符中没有数据和标点符号。
                        doctor_name = next_text
                        break

        return doctor_name

    def parse_other_history(self, recogn_result):
        '''
        分析其他病史，方法是先找到“其他病历"所在行，再找到下一个":",则这中间的都是其他病史。
        :param recogn_result:
        :return:
        '''
        history_str = None
        history_text_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^其他病史",
                                                       end_reg_templ="^体检")
        if history_text_list:
            history_str = "".join(history_text_list)
            self._log.info(
                "[parse_other_history_ok][line_count:{}, result:{}, ]".format(len(history_text_list), history_str))
        else:
            self._log.warning("[parse_other_history_failed][no found]")  # 没有发现开始。

        return history_str

    def parse_treatment_plan(self, recogn_result):
        '''
        治疗处制方案，查找方法，先找到 “治疗处置”，然后再找到“注意事项”四个字，这中间的，都是方案，以“，”分割。
        :param recogn_result:
        :return:
        '''

        history_str = None
        history_text_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^治疗处置",
                                                       end_reg_templ="^注意事项")
        if history_text_list:
            history_str = ",".join(history_text_list)
            self._log.info(
                "[parse_treatment_plan_ok][line_count:{}, result:{}, ]".format(len(history_text_list), history_str))
        else:
            self._log.warning("[parse_treatment_plan_failed][no found]")  # 没有发现开始。

        return history_str


class SchedularBase(ParseBase):
    '''
    用于所有医院调度类的基类
    '''
    pass


class DefaultSchedularBase(SchedularBase):
    '''
    默认医院调度类，当匹配不到医院时，使用此类
    '''

    def get_parse_obj(self):
        '''
        获取基本信息来决定要使用哪个解析器对象。
        :return:
        '''
        return DefaultMedicaRecordParse(log=self._log, recogn_result=self._recogn_result)
