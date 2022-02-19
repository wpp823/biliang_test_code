import asyncio
import time
from bs4 import BeautifulSoup
from pyppeteer import launch


async def get_page(url):
    browser = await launch(headless=False, dumpio=True, autoClose=False, userDataDir='./userdata',
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
    page = await browser.newPage()  # 打开新的标签页
    await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
    await page.goto(url)  # 访问主页
    # evaluate()是执行js的方法，js逆向时如果需要在浏览器环境下执行js代码的话可以利用这个方法
    # js为设置webdriver的值，防止网站检测
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # await page.screenshot({'path': './1.jpg'})  # 截图保存路径
    page_text = await page.content()  # 获取网页源码
    # print(page_text)
    time.sleep(1)
    await browser.close()
    return page_text


product_url = "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.444379c7IPMDYD&id=649768921950&skuId=4859442415879"
html_page = asyncio.get_event_loop().run_until_complete(get_page(product_url))  # 调用

# with open("./test3.html", 'w') as dd:
#     dd.write(html_page)

soup = BeautifulSoup(html_page,'html.parser')
price_tags = soup.find_all('span',class_='tm-price')
for price in price_tags:
    print(f"price_:{price.string}")



