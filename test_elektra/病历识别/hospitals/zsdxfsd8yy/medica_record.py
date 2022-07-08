import re
from typing import Optional

import arrow

from modal import MedicalRecord
from parse_base import ParseBase


class Zsdxfsd8yyMedicaRecord(MedicalRecord):
    """
    中山大学附属第八医院的病历模型
    """
    # 特殊字段
    cur_patient_record: Optional[str]  # 现病史
    history_patient_record: Optional[str]  # 既往史
    person_record: Optional[str]  # 个人史
    marriage_childbirth_record: Optional[str]  # 婚育史
    family_history_record: Optional[str]  # 家族史
    auxiliary_examination: Optional[str]  # 辅助检查


class FirstMedicaRecordParse(ParseBase):
    '''
    中山大学附属第八医院的初诊病历解析
    '''
    re_num = re.compile('\d+')

    def get_medica_record_obj(self) -> Zsdxfsd8yyMedicaRecord:
        '''
        获取病历对象。
        :return:
        '''

        return self._get_medica_record_obj(Zsdxfsd8yyMedicaRecord)

    def parse_hospital_name(self, recogn_result):
        '''
        固化医院名称。
        :param recogn_result:
        :return:
        '''
        return "中山大学附属第八医院"

    def parse_name(self, recogn_result):
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ=".*姓名.*", end_reg_templ=".*性别.*", include_end=True)
        if not t_list:
            return None
        name = "".join([x.strip() for x in t_list]).strip().split("姓名")[1].split("性别")[0].strip()
        return name

    def parse_gender(self, recogn_result):
        '''
        性别
        :param recogn_result:
        :return:
        '''
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ=".*性别.*", end_reg_templ=".*年龄.*", include_end=True)
        if not t_list:
            return None
        name = "".join([x.strip() for x in t_list]).strip().split("性别")[1].split("年龄")[0].strip()
        return name

    def parse_age(self, recogn_result):
        '''
        年龄
        :param recogn_result:
        :return:
        '''

        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ=".*年龄.*", end_reg_templ=".*就诊状态.*", include_end=True)
        if not t_list:
            return None
        name = "".join([x.strip() for x in t_list]).strip().split("年龄")[1].split("就诊状态")[0].strip()
        return name

    def parse_physical_examination(self, recogn_result):
        """
        体检: 对应体格检查
        :param recogn_result:
        :return:
        """
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^体格检查.*", end_reg_templ="^辅助检查.*", include_end=False)
        if not t_list:
            return None
        return "体格检查".join("".join([x.strip() for x in t_list]).strip().split("体格检查")[1:]).strip().strip("：:").strip()

    def parse_inquiry_at(self, recogn_result):
        """
        就诊时间:  原始2021.03.13 09:25 目标: 2021-03-13 09:25
        :param recogn_result:
        :return:
        """
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ=".*就诊日期.*", end_reg_templ=".*就诊科室.*", include_end=True)
        if not t_list:
            return None
        name = "".join([x.strip() for x in t_list]).strip().split("就诊日期")[1].split("就诊科室")[0].strip()
        if not name:
            return None

        re_date = self.re_num
        num_list = re_date.findall(name)

        if len(num_list) == 4 and int(num_list[-2]) >= 100:
            dd_hh = num_list[-2]
            mm = num_list[-1]
            num_list[-2] = dd_hh[:-2]
            num_list[-1] = dd_hh[-2:]
            num_list.append(mm)

        if len(num_list) == 5:
            return arrow.Arrow(
                int(num_list[0]), int(num_list[1]), int(num_list[2]), hour=int(num_list[3]), minute=int(num_list[4])
            ).replace(tzinfo="Asia/Shanghai").format("YYYY-MM-DD HH:mm")

        return None

    def parse_department_name(self, recogn_result):
        '''
        就诊科室
        :param recogn_result:
        :return:
        '''
        name = self._parse_complex_after(recogn_result=recogn_result, begin_reg_templ="^就诊科室", include_begin=True).split("就诊科室")[1]
        name = name.strip().strip("：:").strip()
        if name:
            return name

        return None

    def parse_regist_no(self, recogn_result):
        '''
        就诊登记号
        :param recogn_result:
        :return:
        '''
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ=r".*门诊病历.*", end_reg_templ=".*就诊日期.*", include_end=True)
        if not t_list:
            return None

        text = "".join(t_list).split("门诊病历")[1].split("就诊日期")[0]
        result = self.re_num.search(text)
        if result is None:
            return None

        return result.group()

    def _parse_item_v1(self, recogn_result, item_name: str, next_item_name: str):
        """ """
        item_name_list = ["主诉", "现病史", "既往史", "个人史", "婚育史", "家族史", "体格检查", "辅助检查", "临床诊断", "处置"]
        if next_item_name not in item_name_list:
            exclude_re_if_end_not_found = None
        else:
            index = item_name_list.index(next_item_name)
            if index == len(item_name_list) - 1:
                exclude_re_if_end_not_found = None
            else:
                exclude_re_if_end_not_found = '.*({})[：:]'.format("|".join([f'({x})' for x in item_name_list[index:]]))
        t_list = self._parse_complex_middle_v2(
            recogn_result=recogn_result,
            begin_reg_templ=f"^{item_name}.*",
            end_reg_templ=f"^{next_item_name}.*",
            include_end=False,
            exclude_re_if_end_not_found=exclude_re_if_end_not_found,
        )
        if not t_list:
            return None
        return item_name.join("".join([x.strip() for x in t_list]).strip().split(item_name)[1:]).strip().strip("：:").strip()

    def parse_patient_tells(self, recogn_result):
        """
        主诉
        :param recogn_result:
        :return:
        """
        return self._parse_item_v1(recogn_result=recogn_result, item_name="主诉", next_item_name="现病史")

    def parse_medical_allergy(self, recogn_result):
        '''
        过敏史
        :param recogn_result:
        :return:
        '''
        return None

    def parse_cmd(self, recogn_result):
        '''
        中医诊断
        :param recogn_result:
        :return:
        '''
        return None

    def parse_wmd(self, recogn_result):
        '''
        西医诊断
        :param recogn_result:
        :return:
        '''
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^临床诊断.*", end_reg_templ="^处置.*", include_end=False)
        if not t_list:
            return None

        return "临床诊断".join("".join([x.strip() for x in t_list]).strip().split("临床诊断")[1:]).strip().strip("：:").strip()

    def parse_doctor_name(self, recogn_result):
        """
        医生姓名，获取过程，是先找到“签字盖章”四个字，然后找其前一个和后两个解决出来的对象，根据这两个对象的长度来进行预判是否为名称。
        :param recogn_result:
        :return:
        """
        return None

    def parse_other_history(self, recogn_result):
        '''
        分析其他病史，方法是先找到“其他病历"所在行，再找到下一个":",则这中间的都是其他病史。
        :param recogn_result:
        :return:
        '''
        return None

    def parse_treatment_plan(self, recogn_result):
        """
        治疗处制方案，查找方法，先找到 “治疗处置”，然后再找到“注意事项”四个字，这中间的，都是方案，以“，”分割。
        :param recogn_result:
        :return:
        """
        t_list = self._parse_complex_middle(recogn_result=recogn_result, begin_reg_templ="^处置：:", end_reg_templ="^医师签名.*", include_end=False)
        if not t_list:
            return None
        return "".join([x.strip() for x in t_list]).strip().strip("：:").strip()

    def parse_cur_patient_record(self, recogn_result):
        # 现病史
        return self._parse_item_v1(recogn_result=recogn_result, item_name="现病史", next_item_name="既往史")

    def parse_history_patient_record(self, recogn_result):
        # 既往史
        return self._parse_item_v1(recogn_result=recogn_result, item_name="既往史", next_item_name="个人史")

    def parse_person_record(self, recogn_result):
        # 个人史
        return self._parse_item_v1(recogn_result=recogn_result, item_name="个人史", next_item_name="婚育史")

    def parse_marriage_childbirth_record(self, recogn_result):
        # 婚育史
        return self._parse_item_v1(recogn_result=recogn_result, item_name="婚育史", next_item_name="家族史")

    def parse_family_history_record(self, recogn_result):
        # 家族史
        return self._parse_item_v1(recogn_result=recogn_result, item_name="家族史", next_item_name="体格检查")

    def parse_auxiliary_examination(self, recogn_result):
        # 辅助检查
        return self._parse_item_v1(recogn_result=recogn_result, item_name="辅助检查", next_item_name="临床诊断")


class SecondMedicaRecordParse(FirstMedicaRecordParse):
    """
    复诊病历
    """
    pass


class MixMedicalRecordParse(SecondMedicaRecordParse):
    pass
