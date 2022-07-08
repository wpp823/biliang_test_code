import re

import arrow

from modal import MedicalRecord
from parse_base import ParseBase


class GzzyydxszyyMedicaRecord(MedicalRecord):
    '''
    广州中医院大学深圳医院的病历模型
    '''
    pass


class FirstMedicaRecordParse(ParseBase):
    '''
    广州中医院大学深圳医院的初诊病历解析
    '''

    def get_medica_record_obj(self) -> GzzyydxszyyMedicaRecord:
        '''
        获取病历对象。
        :return:
        '''
        return self._get_medica_record_obj(GzzyydxszyyMedicaRecord)

    def parse_hospital_name(self, recogn_result):
        '''
        固化医院名称。
        :param recogn_result:
        :return:
        '''
        return "广州中医药大学深圳医院（福田）"

    def parse_name(self, recogn_result):
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^姓名[：\s:]*(.+)$", group=1)

    def parse_gender(self, recogn_result):
        '''
        性别
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^性别[：\s:]*(.+)$", group=1)

    def parse_age(self, recogn_result):
        '''
        年龄
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^年龄[：\s:]*([0-9]+)岁$", group=1)

    def parse_physical_examination(self, recogn_result):
        '''
        体格检查
        :param recogn_result:
        :return:
        '''
        physical_text_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^体格检查",
                                                        end_reg_templ="^辅助检查")

        history_str = None
        if physical_text_list:
            history_str = "".join(physical_text_list)
            history_str = history_str[5:]
            self._log.info(
                "[parse_physical_examination_ok][line_count:{}, result:{}, ]".format(len(physical_text_list), history_str))
        else:
            self._log.warning("[parse_physical_examination_failed][no found]")  # 没有发现开始。

        return history_str

        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^体检[：\s:]*(.+)$", group=1)

    def parse_inquiry_at(self, recogn_result):
        '''
        就诊时间
        :param recogn_result:
        :return:
        '''
        at_str = self._parse_simple_regex(recogn_result=recogn_result, regex_template=r"^就诊时间[：\s:]*(.+)$", group=1)
        if at_str:
            at_obj = arrow.get(at_str, "YYYY年MM月DD日HH:mm")
            at_obj.format("YYYY-MM-DD HH:mm")
            return at_obj.format("YYYY-MM-DD HH:mm")
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
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^中医诊断(.+?)[：\s:]*(.+)$", group=2)

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

        re_obj = re.compile("^医师签名")
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
        history_text_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^现病史",
                                                       end_reg_templ="^过敏")
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
                                                       end_reg_templ="^温馨提示")
        if history_text_list:
            history_str = ",".join(history_text_list)
            self._log.info(
                "[parse_treatment_plan_ok][line_count:{}, result:{}, ]".format(len(history_text_list), history_str))
        else:
            self._log.warning("[parse_treatment_plan_failed][no found]")  # 没有发现开始。

        return history_str


class SecondMedicaRecordParse(FirstMedicaRecordParse):
    '''
    复诊病历
    '''

    def parse_other_history(self, recogn_result):
        '''
        分析其他病史，方法是先找到“个人史"所在行，再找到下一个"注意事项",则这中间的都是其他病史。
        :param recogn_result:
        :return:
        '''
        history_str = None
        history_text_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^个人史",
                                                       end_reg_templ="^注意事项")
        if history_text_list:
            history_str = "".join(history_text_list)
            self._log.info(
                "[parse_other_history_ok][line_count:{}, result:{}, ]".format(len(history_text_list), history_str))
        else:
            self._log.warning("[parse_other_history_failed][no found]")  # 没有发现开始。

        return history_str

    def parse_treatment_plan(self, recogn_result):
        '''
        治疗处制方案，查找方法，先找到 “治疗处置”，然后再找到“个人史”四个字，这中间的，都是方案，以“，”分割。
        :param recogn_result:
        :return:
        '''

        history_str = None
        history_text_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^治疗处置",
                                                       end_reg_templ="^个人史")
        if history_text_list:
            history_str = ",".join(history_text_list)
            self._log.info(
                "[parse_treatment_plan_ok][line_count:{}, result:{}, ]".format(len(history_text_list), history_str))
        else:
            self._log.warning("[parse_treatment_plan_failed][no found]")  # 没有发现开始。

        return history_str


class MixMedicalRecordParse(SecondMedicaRecordParse):
    pass
