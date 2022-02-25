import asyncio
import logging
import random
import time

from mongoengine import connection, register_connection
from pyppeteer import launch
# from pz.tools.logger import get_logger

from retrying import retry  # 设置重试次数用的

from my_log import get_logger


class PriceToolsPyppeteer():
    def __init__(self, log):
        self.log = log

    async def get_price(self, url):
        browser = await launch(headless=False, dumpio=True, autoClose=False, userDataDir='./userdata', slowMo=10,
                               args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
        price_list = []
        try:
            page = await browser.newPage()  # 打开新的标签页
            await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
            await page.goto(url)  # 访问产品页
            # 替换淘宝在检测浏览时采集的一些参数。
            # 就是在浏览器运行的时候，始终让window.navigator.webdriver=false
            # navigator是windiw对象的一个属性，同时修改plugins，languages，navigator 且让
            await page.evaluate(
                '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
            await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
            await page.evaluate(
                '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
            await page.evaluate(
                '''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

            # await page.screenshot({'path': './1.jpg'})  # 截图保存路径
            # 滑动屏幕
            # await page.evaluate('window.scrollTo(0,document.body.scrollHeight)')

            # 出现滑动验证 #todo //*[@id="nc_1__scale_text"]/span
            iframe_element = await page.Jx('//*[@id="nc_1__scale_text"]/span')
            if iframe_element:
                self.log.info("出现滑动验证")
                await mouse_slide(page=page)

            # 出现弹出式登录框 #todo
            iframe_element = await page.J('iframe#baxia-dialog-content')
            if iframe_element:
                self.log.info("出现登录框")
            # is_login_ifrom = await page.xpath('//*[@id="container"]')
            # if iframe_element:
            #     # fm-login-id //*[@id="fm-login-id"]   //*[@id="fm-login-id"]
            #     login_id = await page.Jx('//*[@id="fm-login-id"]')
            #     login_id = await page.Jx('//*[@id="fm-login-id"]')
            #     await page.type('//*[@id="fm-login-id"]', '比量1234', {'delay': 120})  # 账号
            #     # await asyncio.sleep(random.randint(1,5))
            #     await page.type('#fm-login-password', 'pzzh123456', {'delay': 120})  # 密码
            #     # await asyncio.sleep(random.randint(1,5)) #login-form > div.fm-btn > button
            #     await page.click('#login-form > div.fm-btn > button')
            login_id = await page.xpath('//*[@id="fm-login-id"]')
            if login_id:
                is_login_success = await login_taobao(page=page)
                self.log.info("PriceToolsPyppeteer.login_taobao is_login_success:{} ".format(is_login_success))
            # 判断价格是否加载
            price_1 = await page.xpath('//*[@id="J_StrPriceModBox"]/dd/span')
            price_2 = await page.xpath('//*[@id="J_PromoPrice"]/dd/div/span')
            price_3 = await page.xpath('//*[@id="J_StrPrice"]/em[2]')
            price_objs = price_1 + price_2 + price_3

            if price_1 or price_2 or price_3:
                # page_text = await page.content()  # 获取网页源码
                price_list = [await (await item.getProperty('textContent')).jsonValue() for item in price_objs]
                self.log.info("[PriceToolsPyppeteer.get_page_ok][url:{},price_list:{}]".format(url, price_list))
                await asyncio.sleep(random.randint(1, 5))
        except:
            self.log.exception("[get_price]")
            await asyncio.sleep(random.randint(1, 5))
        await asyncio.sleep(random.randint(1, 5))
        await browser.close()
        return price_list


async def login_taobao(page=None):
    """
    异步登录方法

    """
    await asyncio.sleep(2)
    try:
        # await page.type('#fm-login-id', '化羽而蒙', {'delay': 120})  # 账号
        await page.type('#fm-login-id', '比量1234', {'delay': 120})  # 账号
        await page.type('#fm-login-password', 'pzzh123456', {'delay': 120})  # 密码
        # await page.type('#fm-login-password', 'w836289789', {'delay': 120})  # 密码
        await page.click('#login-form > div.fm-btn > button')
        await asyncio.sleep(random.randint(1, 5))
    except:
        # await asyncio.sleep(random.randint(1, 5))
        # await browser.close()
        return False
    # await page.close()
    # await browser.close()
    return True


# def retry_if_result_none(result):
#     return result is None
#

async def iframe_id2frame(iframe_id, page):
    iframe_element = await page.J(iframe_id)
    if iframe_element:
        iframe = await iframe_element.contentFrame()
        return iframe
    else:
        return None


# @retry(retry_on_result=retry_if_result_none, )
async def mouse_slide(page=None):
    await asyncio.sleep(2)
    try:
        # 鼠标移动到滑块，按下，滑动到头（然后延时处理），松开按键
        await page.hover('*[@id="nc_1__scale_text"]/span')  # 不同场景的验证码模块能名字不同。//*[@id="nc_1__scale_text"]/span
        await page.mouse.down()
        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        await page.mouse.up()
    except Exception as e:
        print(e, ':验证失败')
        return None, page
    else:
        await asyncio.sleep(2)
        # 判断是否通过
        slider_again = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
        if slider_again != '验证通过':
            return None, page
        else:
            # await page.screenshot({'path': './headless-slide-result.png'}) # 截图测试
            print('验证通过')
            return 1, page


if __name__ == "__main__":
    MONGO_HOST_PART = "mongodb://root:Pzzh4Adminin@192.168.1.230"  # 230
    # MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com:3717"  # 测试服
    # MONGO_HOST_PART  = "mongodb://root:pzzh123456@dds-wz982bab2e6c05b41845-pub.mongodb.rds.aliyuncs.com:3717" # 正式服
    MONGO_HOST_AUTH_DB = "admin"
    MONGO_HOST_REPLICA_SET = None

    MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
    MONGO_DB_NAME = 'nightcrawler'

    register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB,
                        replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)
    log = get_logger(name='PriceToolsPyppeteer.log', log_path='./')
    # log = get_logger()
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=logging.INFO)
    console_handler.setFormatter(logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M'))
    #
    logger.addHandler(time_rotate_file)
    log.addHandler(console_handler)
    # log = log

    # log = get_logger(name="PriceToolsPyppeteer.log", log_path="./")
    price_tool = PriceToolsPyppeteer(log=log)
    update_ret = None
    add_ret = None
    ext_price_info = None
    # ext_url = "https://item.taobao.com/item.htm?id=619300880358"
    ext_url = "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264"
    # product_dao = ProductDao(log=log)
    # product_ext_urls = product_dao.get_product_list(fields=[ProductModel.skus.name, ProductModel.product_id.name])
    product_ext_urls = [ext_url]

    for item in product_ext_urls:
        # product_id = product.product_id
        # for sku in product.skus:
        #     ext_url = sku.ext_url
        #     sku_id = sku.sku_id
        #     log.info(f"product_id:{product_id},sku_id:{sku_id},ext_url:{ext_url}")
        try:
            # 重复三次获取无数据时报错
            for i in range(3):
                time.sleep(random.randint(1, 4))
                # html_page = asyncio.get_event_loop().run_until_complete(price_tool.login())  # 调用
                ext_page_info = asyncio.get_event_loop().run_until_complete(price_tool.get_price(url=ext_url))  # 调用
                # price_tool.get_price(url=ext_url)
                if ext_page_info:
                    price = min([int(float(item)) for item in ext_page_info])
                    log.info(f"product_id:{item}   price:{price}")
                    # break
                # # else:
                # #     time.sleep(random.randint(1, 4))
                # #     ext_price_info = asyncio.get_event_loop().run_until_complete(price_tool.login_taobao())
                # #     log.info(
                #         "[sync_third_party_product_price][login_taobao][ext_price_info:{}]".format(ext_price_info))
        except:
            log.exception("[sync_third_party_product_price_error][ext_url:{}]".format(ext_url))
