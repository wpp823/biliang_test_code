import os

from aip import AipSpeech

BAIDU_APP_ID = '25157501'
BAIDU_API_KEY = "WBiInMMaEWWlLGWhgMNkMWG4"
BAIDU_SECRET_KEY = "dYGwjWqcW155TWzbF07S3tAkYrzNqtP8"


class BaiduAsrTool:
    def __init__(self):
        # self.log = log
        # 百度语音识别

        self._client = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)

    def get_voice_text(self, voice_file_path: str, voice_file_name: str):
        """
        获取语音识别文字
        :param voice_file_path:   语音文件路径
        :param voice_file_name:   语音文件名称
        :return: 识别文字
        """
        file = "{}/{}".format(voice_file_path, voice_file_name)
        with open(file, "rb") as ff:
            voice_file = ff.read()
        res = self._client.asr(voice_file, 'pcm', 16000, {
            'dev_pid': 1537,
        })
        if res.get("err_no") == 0:
            voice_text = res.get("result", "")
        else:
            print("[BaiduAsrTool.get_voice_text_fail],[voice_file_len:{},res:{}]".format(len(voice_file), res))
            voice_text = ""

        return voice_text


if __name__=="__main__":
    tool = BaiduAsrTool()
    voice_file_path = os.path.abspath(r"./")
    voice_file_name = "silk_client/source.pcm"
    tool.get_voice_text(voice_file_path,voice_file_name)