# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Testa1688Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy_demo.Field()

    title = scrapy.Field()  # 标题
    company = scrapy.Field()  # 公司
    price = scrapy.Field()  # 售价
    sell = scrapy.Field()  # 30天成交量
    method = scrapy.Field()  # 销售模式
    rebuy = scrapy.Field()  # 回头率
    address = scrapy.Field()  # 地址
    subicon = scrapy.Field()  # 服务保障
