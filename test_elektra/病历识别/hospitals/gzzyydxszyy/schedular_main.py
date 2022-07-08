from gzzyydxszyy.medica_record import FirstMedicaRecordParse, SecondMedicaRecordParse, MixMedicalRecordParse
from parse_base import SchedularBase


class GzzyydxszyySchedular(SchedularBase):
    def __init__(self, log, recogn_result):
        super(GzzyydxszyySchedular, self).__init__(log=log, recogn_result=recogn_result)

        self._map = {
            "初诊病历": FirstMedicaRecordParse,
            "复诊病历": SecondMedicaRecordParse

        }

    def get_parse_obj(self):
        '''
        获取基本信息来决定要使用哪个解析器对象。
        :return:
        '''
        record_parse_obj = None
        # 获取病历类型名称。
        record_type_name = self._parse_simple_regex(recogn_result=self._recogn_result, regex_template=r'[复初]诊病历', group=0, match=False)
        record_parse_class = self._map.get(record_type_name, MixMedicalRecordParse)
        if record_parse_class:
            record_parse_obj = record_parse_class(log=self._log, recogn_result=self._recogn_result)
            self._log.info("[GzzyydxszyySchedular.get_parse_obj][ok]record_tpye_name:{}]".format(record_type_name))
        else:
            self._log.warning("[GzzyydxszyySchedular.get_parse_obj][failed,msg:暂不支持此种格式的数据][record_tpye_name:{}]".format(record_type_name))

        return record_parse_obj
