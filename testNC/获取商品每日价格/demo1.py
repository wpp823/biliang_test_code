import logging
import time

import pyautogui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import ActionChains, ChromeOptions

pyautogui.PAUSE = 0.5

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

"""
微信公众号 JackCui-AI
更多精彩教程、源码尽在微信公众号
"""


class taobao():
    def __init__(self):

        option = ChromeOptions()
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument("--disable-blink-features")
        option.add_argument("--disable-blink-features=AutomationControlled")

        self.domain = 'https://tmall.com/'
        self.browser = webdriver.Chrome("./chromedriver", options=option)
        # 最大化窗口
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.action_chains = ActionChains(self.browser)

    def get_product_url(self, url):
        username = ""
        password = ""
        self.browser.get(url)

        # self.browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
        self.browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(username)
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
        time.sleep(3)
        try:
            # 出现验证码，滑动验证
            slider = self.browser.find_element_by_class_name("nc-lang-cnt")
            if slider.is_displayed():  # <span class="nc-lang-cnt" data-nc-lang="_startTEXT">请按住滑块，拖动到最右边</span>
                    # 拖拽滑块
                self.action_chains.drag_and_drop_by_offset(slider, 258, 0).perform()
                time.sleep(0.5)
                # 释放滑块，相当于点击拖拽之后的释放鼠标
                self.action_chains.release().perform()
        except (NoSuchElementException, WebDriverException):
            logger.info('未出现登录验证码')

        # 会xpath可以简化点击登陆按钮，但都无法登录，需要使用 pyautogui 完成点击事件
        self.browser.find_element_by_class_name('password-login').click()
        self.browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
        # 图片地址
        # coords = pyautogui.locateOnScreen('./1.png')
        # x, y = pyautogui.center(coords)
        # pyautogui.leftClick(x, y)
        #
        # nickname = self.get_nickname()
        # if nickname:
        #     logger.info('登录成功，呢称为:' + nickname)
        #
        # logger.debug('登录出错，5s后继续登录')
        time.sleep(5)
        # 获取价格
        product_price_ele =  self.browser.find_element_by_xpath('//*[@id="J_PromoPrice"]/dd/div/span')
        print(product_price_ele.text)



    def login(self, username, password):
        while True:

            self.browser.get(self.domain)
            time.sleep(2)

            # 会xpath可以简化这几步
            # self.browser.find_element_by_class_name('h').click()
            # self.browser.find_element_by_id('fm-login-id').send_keys(username)
            # self.browser.find_element_by_id('fm-login-password').send_keys(password)
            self.browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
            self.browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(username)
            self.browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
            time.sleep(1)

            try:
                # 出现验证码，滑动验证
                slider = self.browser.find_element_by_xpath("//span[contains(@class, 'btn_slide')]")
                if slider.is_displayed():
                    # 拖拽滑块
                    self.action_chains.drag_and_drop_by_offset(slider, 258, 0).perform()
                    time.sleep(0.5)
                    # 释放滑块，相当于点击拖拽之后的释放鼠标
                    self.action_chains.release().perform()
            except (NoSuchElementException, WebDriverException):
                logger.info('未出现登录验证码')

            # 会xpath可以简化点击登陆按钮，但都无法登录，需要使用 pyautogui 完成点击事件
            # self.browser.find_element_by_class_name('password-login').click()
            # self.browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
            # 图片地址
            coords = pyautogui.locateOnScreen('1.png')
            x, y = pyautogui.center(coords)
            pyautogui.leftClick(x, y)

            nickname = self.get_nickname()
            if nickname:
                logger.info('登录成功，呢称为:' + nickname)
                break
            logger.debug('登录出错，5s后继续登录')
            time.sleep(5)

    def get_nickname(self):
        self.browser.get(self.domain)
        time.sleep(0.5)
        try:
            return self.browser.find_element_by_class_name('site-nav-user').text
        except NoSuchElementException:
            return ''

    def clear_cart(self):
        cart = self.browser.find_element_by_xpath('//*[@id="J_MiniCart"]')
        if cart.is_displayed():
            cart.click()
        select = self.browser.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label')
        if select.is_displayed():
            select.click()
        time.sleep(0.5)
        go = self.browser.find_element_by_xpath('//*[@id="J_Go"]')
        if go.is_displayed():
            go.click()
        submit = self.browser.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]')
        if submit.is_displayed():
            submit.click()


if __name__ == '__main__':
    # 填入自己的用户名，密码
    # username = 'username'
    # password = 'password'
    tb = taobao()
    # tb.login(username, password)
    url = "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264&skuId=4430618975202"
    tb.get_product_url(url)
