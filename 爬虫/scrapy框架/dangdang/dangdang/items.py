# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图片
    src = scrapy.Field()
    # 书名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
