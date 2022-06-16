import logging

from selenium import webdriver
from selenium.webdriver import ActionChains, ChromeOptions

# logger = logging.getLogger(__name__)
from my_log import get_logger


class GetUserData():
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.log = get_logger()
        option = ChromeOptions()

        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        option.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')
        # 引用header头
        option.add_experimental_option('excludeSwitches', ['enable-automation'])

        # option.add_argument("--disable-blink-features")
        option.add_argument("--disable-blink-features=AutomationControlled")
        # option.add_argument('--proxy-server=http://' + proxy)
        # option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        self.browser = webdriver.Chrome("./chromedriver", options=option)
        # with open('./stealth.min.js') as f:
        #     js = f.read()
        # # 读取js
        # self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": js
        # })
        self.browser.set_window_size(900, 500)
        # self.browser.implicitly_wait(5)
        # self.browser.set_page_load_timeout(10)  # 页面加载超时
        self.action_chains = ActionChains(self.browser)
        self.log.info("init... ")

    def get_login_qrcode(self):
        """获取登录的二维码"""
        self.browser.get(url="https://shop.weixin.qq.com/")
        self.browser.maximize_window()
        self.browser.get_screenshot_as_file("./login_qrcode.png")





    def get_admin_cookie(self):
        """获取登录的cookie"""

        self.browser.get_cookies()

    def get_ext_user_data(self,order_id):
        """获取扩展数据"""

if __name__ == '__main__':
    tools = GetUserData()
    tools.get_login_qrcode()

    tools.get_admin_cookie()
