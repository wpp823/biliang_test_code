import re

from modal import MedicalRecord
from parse_base import DefaultMedicaRecordParse


class SzszyyMedicaRecord(MedicalRecord):
    '''
    深圳市中医院的病历模型
    '''
    pass


class FirstMedicaRecordParse(DefaultMedicaRecordParse):
    '''
    深圳市中医院的初诊病历解析
    '''

    def get_medica_record_obj(self) -> SzszyyMedicaRecord:
        '''
        获取病历对象。
        :return:
        '''

        return self._get_medica_record_obj(SzszyyMedicaRecord)

    def parse_hospital_name(self, recogn_result):
        '''
        固化医院名称。
        :param recogn_result:
        :return:
        '''
        return "深圳市中医院"

    def parse_age(self, recogn_result):
        '''
        年龄
        :param recogn_result:
        :return:
        '''
        age = None
        age_str = self._parse_simple_regex(recogn_result=recogn_result, regex_template=r"年龄[：\s:]*(([0-9]+)岁((([0-9]+)月)|))", group=1, match=False)
        if age_str:
            match_res = re.match(r'(?P<year>[0-9]+)岁(((?P<month>[0-9]+)月)|)', age_str)

            year = match_res.group("year")
            month = match_res.group("month")
            age = '{}'.format(year)
            if month:
                age = "{}.{}".format(year, month)

            # age = "{:.1f}".format(age_float)

        self._log.info("[parse_age][age:{}]".format(age))

        return age


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


class PrescriptionRecordParse(FirstMedicaRecordParse):
    """ 处方笺 """

    pass

class MixMedicalRecordParse(SecondMedicaRecordParse):
    pass
