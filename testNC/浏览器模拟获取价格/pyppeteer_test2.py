import asyncio
import time

from bs4 import BeautifulSoup
from pyppeteer import launch


class PriceToolsPyppeteer():
    def __init__(self):
        pass

    async def get_page(self, url):
        browser = await launch(headless=True, dumpio=True, autoClose=False, userDataDir='./userdata',
                               args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
        page = await browser.newPage()  # 打开新的标签页
        await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
        await page.goto(url)  # 访问产品也
        page_text = None
        await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
        # await page.screenshot({'path': './1.jpg'})  # 截图保存路径
        # 判断价格是否加载
        price_1 = page.xpath('//*[@id="J_StrPriceModBox"]/dd/span').cr_await
        price_2 = page.xpath('//*[@id="J_PromoPrice"]/dd/div/span').cr_await
        if price_1 or price_2:
            page_text = await page.content()  # 获取网页源码
            print(page_text)
            time.sleep(1)
        await browser.close()
        return page_text

    async def login(self):
        browser = await launch(headless=False, dumpio=True, autoClose=False, userDataDir='./userdata',
                               args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
        page = await browser.newPage()
        try:
            # await page.setViewport({'width': 1920, 'height': 1080})
            # login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/'
            # await page.goto('https://login.taobao.com/member/login.jhtml')
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

    def parse_product_price(self, html):
        """
        解析价格

        :param html:
        :return:
        """
        price_list = []
        soup = BeautifulSoup(html, 'html.parser')
        price_tags = soup.find_all('span', class_='tm-price')
        if price_tags:
            price_list.append(int(price.string) for price in price_tags)

        return price_list


if __name__ == "__main__":
    tool = PriceToolsPyppeteer()
    product_url = "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.444379c7IPMDYD&id=649768921950&skuId=4859442415879"
    html_page = asyncio.get_event_loop().run_until_complete(tool.login())  # 调用
    # html_page = asyncio.get_event_loop().run_until_complete(tool.get_page(product_url))  # 调用

#
