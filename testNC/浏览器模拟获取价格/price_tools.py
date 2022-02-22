import asyncio
import time

from pyppeteer import launch

from my_log import get_logger


class PriceToolsPyppeteer():
    def __init__(self, log):
        self.log = log

    async def get_page(self, url):
        browser = await launch(headless=True, dumpio=True, autoClose=False, userDataDir='./userdata',
                               args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
        page = await browser.newPage()  # 打开新的标签页
        await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
        await page.goto(url)  # 访问产品也
        price_list = []
        await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
        # await page.screenshot({'path': './1.jpg'})  # 截图保存路径
        # 判断价格是否加载
        price_1 = await page.xpath('//*[@id="J_StrPriceModBox"]/dd/span')
        price_2 = await page.xpath('//*[@id="J_PromoPrice"]/dd/div/span')
        price_3 = await page.xpath('//*[@id="J_StrPrice"]/em[2]')
        price_objs = price_1 + price_2 + price_3
        # for item in price_3:
        #     self.log.info(item.getProperties())
        if price_1 or price_2 or price_3:
            # page_text = await page.content()  # 获取网页源码
            price_list = [await (await item.getProperty('textContent')).jsonValue() for item in price_objs]
            self.log.info("[PriceToolsPyppeteer.get_page_ok][url:{},price_list:{}]".format(url, price_list))
            time.sleep(1)
        await browser.close()
        return price_list

    async def login_taobao(self):
        browser = await launch(headless=True, dumpio=True, autoClose=False, userDataDir='./userdata',
                               args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
        page = await browser.newPage()
        try:
            # await page.setViewport({'width': 1920, 'height': 1080})
            # login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/'
            await page.goto('https://login.taobao.com/member/login.jhtml')
            await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
            await page.type('#fm-login-id', '比量1234')  # 账号
            await page.type('#fm-login-password', 'pzzh123456')  # 密码
            await asyncio.sleep(5)
            await page.click('#login-form > div.fm-btn > button')
            # await asyncio.sleep(5)
        except:

            return False
        await page.close()
        await browser.close()
        return True



if __name__ == "__main__":
    log = get_logger()
    price_tool = PriceToolsPyppeteer(log=log)
    update_ret = None
    add_ret = None
    ext_price_info = None
    ext_url = "https://item.taobao.com/item.htm?id=619300880358"

    try:
        # 重复三次获取无数据时报错
        for i in range(3):
            # html_page = asyncio.get_event_loop().run_until_complete(price_tool.login())  # 调用
            price_list = asyncio.get_event_loop().run_until_complete(price_tool.get_page(url=ext_url))  # 调用
            # price_list = price_tool.get_page(url=ext_url)
            log.info(f"ext_url:{ext_url}  price_list:{price_list}")
            if price_list:
                price = min([int(item) for item in price_list])
                log.info(f"ext_url:{ext_url}  price:{price}")
                break
            else:
                ext_price_info = asyncio.get_event_loop().run_until_complete(price_tool.login_taobao())
    except:
        log.exception("[sync_third_party_product_price_error][ext_url:{}]".format(ext_url))
