import csv
import logging
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains, ChromeOptions

# logger = logging.getLogger(__name__)
from my_log import get_logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = get_logger()

option = ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features")
option.add_argument("--headless")
option.add_argument("--disable-blink-features=AutomationControlled")
# option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
browser = webdriver.Chrome("./chromedriver", options=option)
# 最大化窗口
browser.set_window_size(1000, 800)
# self.browser.implicitly_wait(5)
# self.browser.set_page_load_timeout(10)  # 页面加载超时
action_chains = ActionChains(browser)
log.info("Tmall init ")
browser.get(url="http://tool.manmanbuy.com/HistoryLowest.aspx")


def is_element_exist(element):
    """
     该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    :param element:
    :return:
    """
    flag = True
    try:
        browser.find_element_by_xpath(element)
        log.info(f"is_element_exist {element} flag:{flag}")
        return flag
    except:

        flag = False
        log.info(f"is_element_exist {element} flag:{flag}")
        return flag


def get_price(url):
    # product_url = 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264'
    price_ttt = browser.find_element_by_xpath('//*[@id="historykey"]')
    price_ttt.clear()
    price_ttt.send_keys(url)

    # 获取价格
    # browser.find_element_by_xpath('//*[@id="searchHistory"]').click()
    next_btn = browser.find_element_by_xpath('//*[@id="searchHistory"]')
    browser.execute_script("arguments[0].click();", next_btn)

    time.sleep(3)

    if is_element_exist('//*[@id="rectMask"]'):
        yanzheng = browser.find_element_by_xpath('//*[@id="rectMask"]')
        yanzheng.click()
    price_nu = 0
    for i in range(4):
        if is_element_exist('//*[@id="maindiv"]/div[2]/div[1]/div[2]/div[1]/div/span[3]'):
            price = browser.find_element_by_xpath('//*[@id="maindiv"]/div[2]/div[1]/div[2]/div[1]/div/span[3]')
            price_nu = price.text
            log.info(price.text)
            break
        else:
            time.sleep(3)

        if i == 3:
            price_nu = -1
            break


    return price_nu


if __name__ == "__main__":
    products = csv.DictReader(open('./产品天猫链接_20220129_01.csv', 'r'))
    new_products = []
    # tb = Tmall(username=username, password=password)
    # login_res = tb.login()

    for info in products:
        price1 = -1
        price2 = -1
        log.info("product_name:" + info.get("title") + "sku_name: " + info.get("SKU名称"))

        # url1 = info.get("new_url_1")
        url1 = info.get("new_url_1")
        if url1:
            # time.sleep(2)
            log.info("new_url_1:" + url1)
            price1 = get_price(url=url1)
            # log.info("new_url_1:{}".format(new_url_1))
            # info["new_url_1"] = new_url_1

        # url2 = info.get("new_url_2")
        url2 = info.get("new_url_2")
        if url2:
            # time.sleep(2)
            log.info("new_url_2:" + url2)
            price2 = get_price(url=url2)
            # log.info("new_url_2:{}".format(new_url_2))
            # info["new_url_2"] = new_url_2

        info["price1"] = price1
        info["price2"] = price2
        new_products.append(info)
    data = pd.DataFrame(data=new_products)

    data.to_excel('peirce_data.xls', encoding='utf-8')
