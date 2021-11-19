import time

from wechatpy.client import WeChatClient
from wechatpy.session.redisstorage import RedisStorage
from wechatpy.utils import random_string


class WechatTool(object):

    WECHATPY_REDIS_PREFIX = 'wx_smilodon'

    def __init__(self, app_id, app_secret, redis):

        self._app_id = app_id
        self._app_secret = app_secret
        self._redis = redis

    def get_redis_wechat_client(self):
        '''
        获取wechatclient，session存redis
        :param app_id:
        :param app_secret:
        :return:
        '''

        session_interface = RedisStorage(self._redis, prefix=self.WECHATPY_REDIS_PREFIX)
        wechat_client = WeChatClient(self._app_id, self._app_secret, session=session_interface)
        return wechat_client


    def get_jssdk_signature(self, target_url):
        '''
        获取jssdk签名
        :return:
        '''

        noncestr = random_string()
        timestamp = int(time.time())

        # wechat_tool = WechatTool(redis=self._redis, app_id=self._app_id, app_secret=self._app_secret)
        client = self.get_redis_wechat_client()

        ticket_response = client.jsapi.get_jsapi_ticket()
        signature = client.jsapi.get_jsapi_signature(
            noncestr,
            ticket_response,
            timestamp,
            target_url
        )
        signature_data = {
            'noncestr': noncestr,
            'timestamp': timestamp,
            'url': target_url,
            'signature': signature,
            "appid": self._app_id
        }
        return signature_data


if __name__ == "__main__":
    wx_tool = WechatTool(app_id='',app_secret='',redis='')