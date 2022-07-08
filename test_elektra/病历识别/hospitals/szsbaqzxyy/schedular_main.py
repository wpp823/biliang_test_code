from parse_base import SchedularBase
from medica_record import MixMedicalRecordParse


class SzsbaqzxyySchedular(SchedularBase):

    def get_parse_obj(self):
        """
        获取基本信息来决定要使用哪个解析器对象。
        :return:
        """

        # 获取病历类型名称。
        # 使用 ^就诊状态 会因为与前面的内容连接在一起而误判
        record_type_name = self._parse_complex_after(recogn_result=self._recogn_result, begin_reg_templ='.*就诊状态.*', include_begin=False)
        if record_type_name:
            record_type_name = record_type_name.strip().strip("：:").strip()

        record_parse_class = MixMedicalRecordParse
        record_parse_obj = record_parse_class(log=self._log, recogn_result=self._recogn_result)
        self._log.info(f"[{self.__class__.__name__}.get_parse_obj][ok]record_tpye_name:{record_type_name}]")

        return record_parse_obj
