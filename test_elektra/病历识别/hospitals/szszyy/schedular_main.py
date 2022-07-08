from parse_base import SchedularBase
from szszyy.medica_record import FirstMedicaRecordParse, SecondMedicaRecordParse, MixMedicalRecordParse, PrescriptionRecordParse


class SzszyySchedular(SchedularBase):
    def __init__(self, log, recogn_result):
        super(SzszyySchedular, self).__init__(log=log, recogn_result=recogn_result)

        self._map = {
            "门诊初诊病历": FirstMedicaRecordParse,
            "门诊复诊病历": SecondMedicaRecordParse
        }

    def get_parse_obj(self):
        """
        获取基本信息来决定要使用哪个解析器对象。
        :return:
        """
        hospital_name = self.parse_hospital_name(recogn_result=self._recogn_result)

        record_parse_class = None
        record_type_name = ""
        if hospital_name:
            if hospital_name.find("处方") > -1:
                record_parse_class = PrescriptionRecordParse
            elif hospital_name.find('检验科检验报告') > -1:
                pass

        # 获取病历类型名称。
        if not record_parse_class:
            record_type_name = self._parse_simple_regex(recogn_result=self._recogn_result, regex_template='^门诊[复初]诊病历', group=0)
            record_parse_class = self._map.get(record_type_name, MixMedicalRecordParse)

        record_parse_obj = record_parse_class(log=self._log, recogn_result=self._recogn_result)
        self._log.info(
            "[SzszyySchedular.get_parse_obj][ok]record_tpye_name:{}, record_class:{}]".format(record_type_name, record_parse_class.__name__))

        return record_parse_obj
