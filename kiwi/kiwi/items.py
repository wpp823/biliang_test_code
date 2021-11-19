# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KiwiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy_demo.Field()
    pass


class ProductItem(scrapy.Item):
    stock = scrapy.Field()  # 库存
    trade_price = scrapy.Field()  # 产品批发价
    title = scrapy.Field()  # 产品名称
    express_fee = scrapy.Field()  # 快递费用
    spu_id = scrapy.Field()  # 商品id
    sku_id = scrapy.Field()  # 规格属性id
