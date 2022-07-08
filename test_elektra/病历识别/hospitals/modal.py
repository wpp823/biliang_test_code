from typing import Optional

from pydantic import BaseModel


class MedicalRecord(BaseModel):
    '''
    基础病历的对象。
    '''
    hospital_name: Optional[str]  # 医院名称

    name: Optional[str]
    gender: Optional[str]
    age: Optional[str]
    inquiry_at: Optional[str]  # 就诊时间  2021-03-23 09:34
    department_name: Optional[str]  # 就诊科室

    regist_no: Optional[str]  # 登陆号
    patient_tells: Optional[str]  # 主诉
    medical_allergy: Optional[str]  # 过敏史
    cmd: Optional[str]  # 中医诊断
    wmd: Optional[str]  # 西医诊断

    doctor_name: Optional[str]  # 医生名称
    other_history: Optional[str]  # 其他病史

    treatment_plan: Optional[str]  # 治疗方案
    physical_examination: Optional[str]  # 体检 | 体格检查
    inquiry_type: str = "门诊"  # 就诊类型？

    @property
    def is_medical_record(self):
        # 判断是否是病历
        return self.hospital_name
