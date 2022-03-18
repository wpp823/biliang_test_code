#  精斗云 星辰 SDK For Python
* * *
### Python
* * *
#### 要求
* * *
* 要使用 星辰 SDK for Python，您需要一个星辰账号以及一对ClientID和ClientSecret。 请在云平台管理页面上创建和查看您的ClientID，或者联系您的系统管理员。
* 要使用星辰 SDK for Python 之前请先阅读星辰API文档以便了解代码运行流程。
* [精斗云星辰API文档地址](https://cloud.kingdee.com/help/document/detail?item=248&doc=1648)
* * *
#### 模块说明

* * *
星辰 SDK for Python 共分为五大模块
其中 kernel ，auth 为使用时必须引入的包。scm，basedata,fi 看使用情况再确定是否引入。

* kernel（核心包）
* auth（账号账套信息）
* scm(经销存）
* basedata（基础资料）
* fi（财务）

* * *
#### 快速使用

* * *

以下这个代码示例向您展示了调用 星辰 SDK for Python 的3个主要步骤：

1. 第一次使用SDK需要引入几个公用包，需要你的环境安装python,并且安装pip。
2. 使用pip导入第三方包。
    
```
1.pip install alibabacloud-tea-util;

2.pip install tea;
```
3. 创建auth实例并初始化。
4. 创建API请求并设置参数。
5. 发起请求并处理。

```
from auth.kingdeejdy_auth.kingdeejdy_auth import KingdeejdyAuth
from kingdeejdy_kernel.kingdeejdy_kernel.kingdeejdy_kernel import KingdeejdyKernel
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

```

* * *
#### 附加说明
* * *
* 此SDK为1.0版本，目前使用效果不理想，目前正在重构SDK2.0, 1.0版本仅供测试使用，与参考。
* 星辰 SDK 使用多语言工具生生成，示例代码只简便展示，具体使用时可以完善再构建。
* 实例项目在sample目录下。
* 模块包目前没有上pip仓库，需要使用可以自行打包再引入本地仓库，或者使用路径直接引入代码。
* 本SDK为内测版本，如有问题或者需要帮助可以云之家联系邹远发。
* * *
