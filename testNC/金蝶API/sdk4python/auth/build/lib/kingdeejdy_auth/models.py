# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class AccountGroup(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_id: str = None,
        enable: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.account_name = account_name
        self.account_id = account_id
        self.enable = enable
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.enable is not None:
            result['enable'] = self.enable
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        return self


class AccountService(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        service_name: str = None,
        service_addr: str = None,
        account_groups: List[AccountGroup] = None,
    ):
        self.service_id = service_id
        self.service_name = service_name
        self.service_addr = service_addr
        self.account_groups = account_groups
        # 定义类

    def validate(self):
        self.validate_required(self.service_id, 'service_id')
        self.validate_required(self.service_name, 'service_name')
        self.validate_required(self.service_addr, 'service_addr')
        self.validate_required(self.account_groups, 'account_groups')
        if self.account_groups:
            for k in self.account_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_addr is not None:
            result['serviceAddr'] = self.service_addr
        result['accountGroups'] = []
        if self.account_groups is not None:
            for k in self.account_groups:
                result['accountGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceAddr') is not None:
            self.service_addr = m.get('serviceAddr')
        self.account_groups = []
        if m.get('accountGroups') is not None:
            for k in m.get('accountGroups'):
                temp_model = AccountGroup()
                self.account_groups.append(temp_model.from_map(k))
        return self


class TokenResponseData(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        avatar: str = None,
        expires: int = None,
        expires_in: int = None,
        gender: int = None,
        nickname: str = None,
        uid: int = None,
    ):
        self.access_token = access_token
        self.avatar = avatar
        self.expires = expires
        self.expires_in = expires_in
        self.gender = gender
        self.nickname = nickname
        self.uid = uid

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        self.validate_required(self.avatar, 'avatar')
        self.validate_required(self.expires, 'expires')
        self.validate_required(self.expires_in, 'expires_in')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.nickname, 'nickname')
        self.validate_required(self.uid, 'uid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.expires is not None:
            result['expires'] = self.expires
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.gender is not None:
            result['gender'] = self.gender
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('expires') is not None:
            self.expires = m.get('expires')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class TokenResponse(TeaModel):
    """
    auth api response，used to get accesstoken
    """
    def __init__(
        self,
        errcode: int = None,
        description: str = None,
        data: TokenResponseData = None,
    ):
        self.errcode = errcode
        self.description = description
        self.data = data

    def validate(self):
        self.validate_required(self.errcode, 'errcode')
        self.validate_required(self.description, 'description')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.errcode is not None:
            result['errcode'] = self.errcode
        if self.description is not None:
            result['description'] = self.description
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errcode') is not None:
            self.errcode = m.get('errcode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('data') is not None:
            temp_model = TokenResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class AccountGroupRequest(TeaModel):
    """
    AccountGroupRequest
    """
    def __init__(
        self,
        access_token: str = None,
    ):
        self.access_token = access_token

    def validate(self):
        self.validate_required(self.access_token, 'access_token')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        return self


class AccountGroupResponseDataAccountGroups(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_id: str = None,
        enable: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.account_name = account_name
        self.account_id = account_id
        self.enable = enable
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.enable is not None:
            result['enable'] = self.enable
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        return self


class AccountGroupResponseData(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        account_groups: List[AccountGroupResponseDataAccountGroups] = None,
    ):
        self.service_id = service_id
        self.account_groups = account_groups

    def validate(self):
        self.validate_required(self.service_id, 'service_id')
        self.validate_required(self.account_groups, 'account_groups')
        if self.account_groups:
            for k in self.account_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        result['accountGroups'] = []
        if self.account_groups is not None:
            for k in self.account_groups:
                result['accountGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        self.account_groups = []
        if m.get('accountGroups') is not None:
            for k in m.get('accountGroups'):
                temp_model = AccountGroupResponseDataAccountGroups()
                self.account_groups.append(temp_model.from_map(k))
        return self


class AccountGroupResponse(TeaModel):
    def __init__(
        self,
        data: List[AccountGroupResponseData] = None,
        success: bool = None,
        error_code: str = None,
        message: str = None,
    ):
        self.data = data
        self.success = success
        self.error_code = error_code
        self.message = message

    def validate(self):
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AccountGroupResponseData()
                self.data.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


