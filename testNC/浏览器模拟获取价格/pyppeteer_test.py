import logging
from asyncio import sleep, get_event_loop

from pyppeteer import launch

from my_log import get_logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = get_logger()


class TaoBaoSpider:
    def __init__(self):
        self.width, self.height = 1500, 800
        get_event_loop().run_until_complete(self.init())
        get_event_loop().run_until_complete(self.login())
        get_event_loop().run_until_complete(self.open_url())
        # get_event_loop().run_until_complete(self.get_price())

    async def init(self):
        # noinspection PyAttributeOutsideInit
        self.browser = await launch(headless=False,
                                    args=['--disable-infobars', f'--window-size={self.width},{self.height}'],
                                    userDataDir='./userdata')
        # noinspection PyAttributeOutsideInit

        self.page = await self.browser.newPage()
        await self.page.setViewport({'width': self.width, 'height': self.height})
        # await self.page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
        # await self.page.goto('https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264&skuId=4430618975202')
        await self.page.evaluate('()=>{Object.defineProperties(navigator,{webdriver:{get:()=>false}})}')

    @staticmethod
    async def login():
        await sleep(3)

    async def open_url(self):
        new_page = await self.browser.newPage()
        await new_page.goto('https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264&skuId=4430618975202')
        print(new_page.content())

    def get_price(self):
        pass


if __name__ == "__main__":
    tbs = TaoBaoSpider()
    # tbs.open_url()

    # products = csv.DictReader(open('./产品天猫链接_20220129_01.csv', 'r'))
    # new_products = []
    # for info in products:
    #     price1 = -1
    #     price2 = -1
    #     log.info("product_name:" + info.get("title") + "sku_name: " + info.get("SKU名称"))
    #
    #     # url1 = info.get("new_url_1")
    #     url1 = info.get("new_url_1")
    #     if url1:
    #         # time.sleep(2)
    #         log.info("new_url_1:" + url1)
    #         price1 = get_price(url=url1)
    #         # log.info("new_url_1:{}".format(new_url_1))
    #         # info["new_url_1"] = new_url_1
    #
    #     # url2 = info.get("new_url_2")
    #     url2 = info.get("new_url_2")
    #     if url2:
    #         # time.sleep(2)
    #         log.info("new_url_2:" + url2)
    #         price2 = get_price(url=url2)
    #         # log.info("new_url_2:{}".format(new_url_2))
    #         # info["new_url_2"] = new_url_2
    #
    #     info["price1"] = price1
    #     info["price2"] = price2
    #     new_products.append(info)
    # data = pd.DataFrame(data=new_products)
    #
    # data.to_excel('peirce_data.xls', encoding='utf-8')
