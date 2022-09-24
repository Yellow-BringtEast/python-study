import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import DushuItem


class ReadSpider(CrawlSpider):

    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1107_\d+\.html'), callback='parse', follow=False),
    )

    def parse(self, response, **kwargs):
        img_list = response.xpath('//div[@class="bookslist"]//a/img')

        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            pic = img.xpath('./@data-original').extract_first()

            book = DushuItem(name=name, pic=pic)

            yield book
