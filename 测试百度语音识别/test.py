from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '25157501'
API_KEY = 'WBiInMMaEWWlLGWhgMNkMWG4'
SECRET_KEY = 'dYGwjWqcW155TWzbF07S3tAkYrzNqtP8'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

filePath_test = r'msg_2409250708216650049b899101.pcm'
#ffmpeg -y  -i msg_41115609102114676808322103.amr  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 16k.pcm


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
res = client.asr(get_file_content(filePath_test), 'pcm', 8000, {
    'dev_pid': 1537,
})
if res.get("err_no")==0:
    text_result = res.get("result")


