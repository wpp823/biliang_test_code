# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from auth.kingdeejdy_auth.kingdeejdy_auth import KingdeejdyAuth
from kingdeejdy_kernel.kingdeejdy_kernel import KingdeejdyKernel
#基础资料
from business.basedata.kingdeejdy_basedata.kingdeejdy_basedata import KingdeejdyBasedata
#财务
from business.fi.kingdeejdy_fi.kingdeejdy_fi import KingdeejdyFi
#经销存
from business.scm.kingdeejdy_scm.kingdeejdy_scm import KingdeejdyScm


from Tea.model import TeaModel
from alibabacloud_tea_util.client import Client as UtilClient
#基础资料
from business.basedata.kingdeejdy_basedata import models as sdk_bd_models
#财务
from business.fi.kingdeejdy_fi import models as sdk_fi_models
#经销存
from business.scm.kingdeejdy_scm import models as sdk_scm_models



class Sample:
    def __init__(self):
        pass
class TokenRequestQuery(TeaModel):
    """
    登录query

    *\
    """
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        username: str = None,
        password: str = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.client_secret, 'client_secret')
        self.validate_required(self.username, 'username')
        self.validate_required(self.password, 'password')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.client_secret is not None:
            result['client_secret'] = self.client_secret
        if self.username is not None:
            result['username'] = self.username
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self



def main():
        auth = KingdeejdyAuth()
        # 登录参数
        token_request_query = TokenRequestQuery(
            client_id='205022',
            client_secret='1b16d77089b1e60b3f7c907aa3cc612e',
            username='17220202021',
            password='jdy888888'
        )
        # 获取token
        access_token_object = auth.get_token(token_request_query)
        # 获取账套
        account_groups = auth.get_account(access_token_object)
        # 账套可能有多条，这里示例默认取第一条。
        account_service = UtilClient.assert_as_map(account_groups[0])
        groups = UtilClient.assert_as_array(account_service.get('accountGroups'))
        group = UtilClient.stringify_map_value(UtilClient.assert_as_map(groups[0]))
        account_id = group.get('accountId')
        group_name = group.get('groupName')
        access_token = access_token_object.access_token
        kernel = KingdeejdyKernel(access_token, account_id, group_name)
        scm = KingdeejdyScm(kernel)
        body = sdk_scm_models.PurInboundListRequestBody(

         )
        # 获取商品列表示例
        purInboundListRequest = sdk_scm_models.PurInboundListRequest(
            body=body
        )
        response = scm.get_pur_inbound_list(purInboundListRequest)
        print(response)

if __name__ == '__main__':
    main()
