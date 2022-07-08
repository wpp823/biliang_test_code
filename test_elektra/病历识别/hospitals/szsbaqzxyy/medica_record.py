from modal import MedicalRecord
from parse_base import DefaultMedicaRecordParse


class SzsbaqzxyyMedicaRecord(MedicalRecord):
    """
    深圳市宝安区中心医院的病历模型
    """
    patient_phone: str  # 联系电话


class MixMedicalRecordParse(DefaultMedicaRecordParse):
    """
    深圳市宝安区中心医院的初诊病历解析

    # 基于 门(急)诊病历 编写 @202107151750
    """

    def __init__(self, *args, **kwargs):
        super(MixMedicalRecordParse, self).__init__(*args, **kwargs)

        self.item_name_list = [
            "主诉", "现病史", "既往史", "婚育史", "家族史", "过敏史", "体格检查", "辅助检查", "临床诊断", "初步诊断",
            "治疗处置", "处置", "医生签名", "注"
        ]

    def get_medica_record_obj(self) -> SzsbaqzxyyMedicaRecord:
        '''
        获取病历对象。
        :return:
        '''

        return self._get_medica_record_obj(SzsbaqzxyyMedicaRecord)

    def parse_hospital_name(self, recogn_result):
        '''
        固化医院名称。
        :param recogn_result:
        :return:
        '''
        return "深圳市宝安区中心医院"

    def parse_inquiry_at(self, recogn_result):
        """
        就诊时间
        :param recogn_result:
        :return:
        """
        at_str = self._parse_simple_regex(recogn_result=recogn_result, regex_template=r"^就诊日期[：\s:]*([年月日\d\-\:]+)$", group=1)
        if at_str:
            at_list = list(at_str)
            at_list.insert(10, ' ')
            return "".join(at_list)
        return None

    def _parse_item_v1(self, recogn_result, item_name: str, next_item_name: str):
        """ """
        item_name_list = self.item_name_list
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

    def parse_doctor_name(self, recogn_result):
        '''
        医生姓名
        :param recogn_result:
        :return:
        '''
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^医生签名[：\s:]*(.+)$", group=1)

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
        return self._parse_item_v1(recogn_result=recogn_result, item_name="过敏史", next_item_name="体格检查")

    def parse_wmd(self, recogn_result):
        """
        西医诊断
        :param recogn_result:
        :return:
        """
        for key in ["初步诊断", "临床诊断"]:
            value = self._parse_item_v1(recogn_result=recogn_result, item_name=key, next_item_name="治疗处置")
            if value:
                return value

        return None

    def parse_treatment_plan(self, recogn_result):
        '''
        治疗处制方案，查找方法，先找到 “治疗处置”，然后再找到“注意事项”四个字，这中间的，都是方案，以“，”分割。
        :param recogn_result:
        :return:
        '''
        return self._parse_item_v1(recogn_result=recogn_result, item_name="治疗处置", next_item_name="医生签名")

    def parse_patient_phone(self, recogn_result):
        """
        联系电话
        """
        return self._parse_simple_regex(recogn_result=recogn_result, regex_template="^联系电话[：\s:]*(.+)$", group=1)
