import scrapy

from bs4 import BeautifulSoup

from scrapy_demo.A1688.testA1688.testA1688.items import  Testa1688Item

PAGE = '1'


class A1688sellofferspiderSpider(scrapy.Spider):
    name = 'A1688SellofferSpider'
    allowed_domains = ['www.1688.com']
    start_urls = ['http://www.1688.com/']

    def start_requests(self):
        for page in range(1, int(PAGE) + 1):
            url = 'https://detail.1688.com/offer/617510835936.html?spm=a261y.7663282.10811813088311.5.5dea6d19ODCO3U'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 实例化一个数据模型
        item = Testa1688Item()
        for tag in response.css('.sw-dpl-offer-item').extract():
            try:
                # 从response中利用css选择器提取出来的标签是文本形式，需要利用 BeautifulSoup 转换成BeautifulSoup.Tag 对象进行进一步提取。
                soup = BeautifulSoup(tag, 'lxml')

                item['title'] = soup.select(".sw-dpl-offer-photo img")[0].attrs['alt']
                item['company'] = soup.select(".sw-dpl-offer-companyName")[0].attrs['title']
                item['price'] = soup.select(".sw-dpl-offer-priceNum")[0].attrs['title']
                item['sell'] = soup.select(".sm-offer-tradeBt")[0].attrs['title']
                item['rebuy'] = soup.select(".sm-widget-offershopwindowshoprepurchaserate span")[2].string
                item['method'] = soup.select(".sm-widget-offershopwindowshoprepurchaserate i")[0].string
                # 对于不一定能获取的数据，需要判断数据存在与否。
                if soup.select(".sm-offer-location")[0].attrs['title']:
                    address = soup.select(".sm-offer-location")[0].attrs['title']
                else:
                    address = " "
                item['address'] = address

                if soup.select(".sm-offer-subicon a"):
                    subicon = []
                    for i in soup.select(".sm-offer-subicon a"):
                        subicon.append(i.attrs['title'] + ',')
                    print(subicon)
                    item['subicon'] = subicon
                else:
                    item['subicon'] = ' '
                # 返回这个数据模型，交给 ITEM_PIPELINES 处理
                yield item
            except Exception as error:
                yield item
                print("出错了:", error)
                continue
