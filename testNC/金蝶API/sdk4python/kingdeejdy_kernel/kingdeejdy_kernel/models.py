# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import List

from Tea.model import TeaModel


class ApiSaveResponseDataError(TeaModel):
    def __init__(
            self,
            id: str = None,
            msg: str = None,
    ):
        self.id = id
        self.msg = msg

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ApiSaveResponseData(TeaModel):
    def __init__(self, success_pk_ids: List[str] = None, error_info: List[ApiSaveResponseDataError] = None, message: str = None,
                 success: bool = None, error_level: str = None, ):
        self.success_pk_ids = success_pk_ids
        self.error_info = error_info
        self.message = message
        self.success = success
        self.error_level = error_level

    def validate(self):
        self.validate_required(self.success_pk_ids, 'success_pk_ids')
        self.validate_required(self.error_info, 'error_info')
        if self.error_info:
            for k in self.error_info:
                if k:
                    k.validate()
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_level, 'error_level')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_pk_ids is not None:
            result['successPkIds'] = self.success_pk_ids
        result['errorInfo'] = []
        if self.error_info is not None:
            for k in self.error_info:
                result['errorInfo'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.error_level is not None:
            result['errorLevel'] = self.error_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('successPkIds') is not None:
            self.success_pk_ids = m.get('successPkIds')
        self.error_info = []
        if m.get('errorInfo') is not None:
            for k in m.get('errorInfo'):
                temp_model = ApiSaveResponseDataError()
                self.error_info.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorLevel') is not None:
            self.error_level = m.get('errorLevel')
        return self


class ApiSaveResponse(TeaModel):
    def __init__(self,error_code: str = None,message: str = None,success: bool = None,data: ApiSaveResponseData = None,):
        self.error_code = error_code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('data') is not None:
            temp_model = ApiSaveResponseData()
            self.data = temp_model.from_map(m['data'])
        return self
