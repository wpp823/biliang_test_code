from typing import Dict

import requests


class VocelCloudApi():
    """
    体素数据请求基类

    """

    def __init__(self, access_key, secret_key, log):
        self.access_key = access_key
        self.secret_key = secret_key
        self._log = log
        self._host = "https://skin-api.voxelcloud.net.cn/api/"

    def _post(self, url, data: Dict):
        """
        封装post方法

        @param url:
        @param data:
        @return:
        """

        target_url = f'{self._host}{url}'
        res = {}
        try:
            res = requests.post(url=target_url, data=data)
            self._log.info("[VocelCloudApi.post][target_url:{}][params:{}][res:{}]".format(target_url, data, res))
        except:
            self._log.exception("[VocelCloudApi.post_fail][target_url:{}][params:{}]".format(target_url, data))
        return res
