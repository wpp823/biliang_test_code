import csv
import logging
import time

import pandas as pd

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver import ActionChains, ChromeOptions


# logger = logging.getLogger(__name__)
from my_log import get_logger


class Tmall():
    def __init__(self, username, password):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.log = get_logger()
        option = ChromeOptions()
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument("--disable-blink-features")
        option.add_argument("--disable-blink-features=AutomationControlled")
        # option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        self.browser = webdriver.Chrome("./chromedriver", options=option)
        # 最大化窗口
        self.browser.set_window_size(900, 500)
        # self.browser.implicitly_wait(5)
        # self.browser.set_page_load_timeout(10)  # 页面加载超时
        self.action_chains = ActionChains(self.browser)
        self.log.info("Tmall init ")
        self.username = username
        self.password = password

    def is_element_exist(self, element):
        """
         该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        :param element:
        :return:
        """
        flag = True
        try:
            self.browser.find_element_by_xpath(element)
            return flag
        except:
            self.log.info(f"is_element_exist {element}")
            flag = False
            return flag

    def login(self):
        """
        登录天猫，使用某一商品的地址打开，弹出的登录页面，便于查找登录元素
        :param username:
        :param password:
        :return:
        """

        self.browser.get(url="https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264")
        try:
            # //*[@id="fm-login-id"]
            if self.is_element_exist('//*[@id="fm-login-id"]'):
                # self.browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
                self.browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(self.username)
                time.sleep(2)
                self.log.info("get_product_url.login.input.user_name")
                self.browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(self.password)
                self.log.info("get_product_url.login.input.user_pwd")
                time.sleep(2)
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
                    self.log.info('未出现登录验证码')

                # 会xpath可以简化点击登陆按钮，但都无法登录，需要使用 pyautogui 完成点击事件
                self.browser.find_element_by_class_name('password-login').click()
                self.log.info("login in click")
                # 等待点击确认进入
                while not (self.is_element_exist('//*[@id="J_PromoPrice"]/dd/div/span') or self.is_element_exist('//*[@id="J_StrPriceModBox"]/dd/span') or self.is_element_exist(
                        '//*[@id="J_StrPrice"]/em[2]')):
                    self.log.info("等待手机端确认")
                    time.sleep(3)
                return True

            else:
                self.log.info("登录页未打开")
                time.sleep(5)
                self.login()

        except:
            self.log.error("登录报错 ")
            self.del_cookies()
            return False

    def login_popup(self):
        """
        弹出式登录框

        :return:
        """

    def get_price(self, url):
        """
        获取最低价格

        //*[@id="J_PromoPrice"]/dd/div/span 促销价格
        //*[@id="J_StrPriceModBox"]/dd/span 无促销价格情况
        //*[@id="J_StrPrice"]/em[2] 淘宝链接
        :param url:
        :return:
        """
        # self.browser.set_page_load_timeout(5)  # 页面加载超时
        self.browser.quit()  # 清除浏览器缓存
        try:
            try:
                self.browser.get(url=url)
            except TimeoutException:
                self.log.info("停止加载")
                time.sleep(1)

                # time.sleep(5)
                # self.browser.execute_script("window.stop();")
                #
                # while not (self.is_element_exist('//*[@id="J_PromoPrice"]/dd/div/span') or self.is_element_exist('//*[@id="J_StrPriceModBox"]/dd/span') or self.is_element_exist(
                #         '//*[@id="J_StrPrice"]/em[2]')):
                #     self.log.error("无法获取价格")
                #
                #     if self.is_element_exist('//*[@id="fm-login-id"]'):  #//*[@id="fm-login-id"] 需要登录
                #         self.login()
                #         self.browser.get(url=url)

                time.sleep(6)

            # prices = []
            # 获取价格
            time.sleep(2)
            if self.is_element_exist('//*[@id="J_PromoPrice"]/dd/div/span'):  # 促销价
                product_price_ele = self.browser.find_element_by_xpath('//*[@id="J_PromoPrice"]/dd/div/span')
                # prices.append(round(float(product_price_ele.text)))

            elif self.is_element_exist('//*[@id="J_StrPriceModBox"]/dd/span'):  # 无促销价
                product_price_ele = self.browser.find_element_by_xpath('//*[@id="J_StrPriceModBox"]/dd/span')
                # prices.append(round(float(product_price_ele.text)))
            elif self.is_element_exist('//*[@id="J_StrPrice"]/em[2]'):  # 淘宝链接价 #//*[@id="J_StrPrice"]/em[2]
                product_price_ele = self.browser.find_element_by_xpath('//*[@id="J_StrPrice"]/em[2]')
                # prices.append(round(float(product_price_ele.text)))
            else:
                # 无法获取时，清除缓存
                self.log.error("获取价格失败、未找到价格控件")
                return self.browser.current_url, -3
            # time.sleep(3)
            if product_price_ele:
                self.log.info("get_price:{}".format(product_price_ele.text))
                return self.browser.current_url, product_price_ele.text
            else:
                raise Exception
        except Exception as e:
            self.log.exception("获取价格异常 ")
            self.del_cookies()
            time.sleep(3)
            return self.browser.current_url, -2

    def login_out(self):
        pass

    def del_cookies(self):
        # 清除浏览器cookies
        cookies = self.browser.get_cookies()
        self.log.info(f"main: cookies = {cookies}")
        self.browser.delete_all_cookies()


if __name__ == '__main__':
    # 填入自己的用户名，密码,登录时若遇到需要手机淘宝确认的需要提前打开淘宝

    username = 'name'
    password = 'pwd'

    """
    price 为-1时，代表无链接
    price 为-2时，代表获取价格异常
    price 为-3时，商品不存在，或者页面控件xpath不正确
    """

    products = csv.DictReader(open('./产品天猫链接_20220129_01.csv', 'r'))
    new_products = []
    tb = Tmall(username=username, password=password)
    login_res = tb.login()
    if login_res:
        for info in products:
            price1 = -1
            price2 = -1
            tb.log.info("product_name:" + info.get("title") + "sku_name: " + info.get("SKU名称"))

            # url1 = info.get("new_url_1")
            url1 = info.get("天猫链接")
            if url1:
                time.sleep(2)
                tb.log.info("new_url_1:" + url1)
                new_url_1, price1 = tb.get_price(url=url1)
                tb.log.info("new_url_1:{}".format(new_url_1))
                info["new_url_1"] = new_url_1

            # url2 = info.get("new_url_2")
            url2 = info.get("天猫链接2")
            if url2:
                time.sleep(2)
                tb.log.info("new_url_2:" + url2)
                new_url_2, price2 = tb.get_price(url=url2)
                tb.log.info("new_url_2:{}".format(new_url_2))
                info["new_url_2"] = new_url_2

            info["price1"] = price1
            info["price2"] = price2
            new_products.append(info)
        data = pd.DataFrame(data=new_products)

        data.to_excel('peirce_data.xls', encoding='utf-8')
    else:
        tb.log.info("登录失败")
