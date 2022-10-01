import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import Fortune500Item


class FortuneSpider(CrawlSpider):
    name = 'fortune'
    allowed_domains = ['www.fortunechina.com']
    start_urls = ['https://www.fortunechina.com/fortune500/c/2022-08/03/content_415683.htm']

    # 获取所有年份的500强榜单URL
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="swiper-slide"]'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 通过榜单标题，获取年份
        h1 = response.xpath('//h1/text()').extract_first()
        year = h1.strip()[:4]

        tr_list = response.xpath('//tbody/tr')

        for tr in tr_list:
            # 第一类xpath
            rank = tr.xpath('./td[1]/text()').extract_first()
            ent_name = tr.xpath('./td[2]/a/text()').extract_first()
            country = tr.xpath('./td[5]/text()').extract_first()

            # 第一类xpath
            if ent_name is None:
                ent_name = tr.xpath('./td[3]/a[1]/text()').extract_first()
                country = tr.xpath('./td[6]/text()').extract_first()

            # 第二类xpath
            if ent_name is None:
                ent_name = tr.xpath('./td[2]/text()').extract_first()
                country = tr.xpath('./td[3]/text()').extract_first()

            # 第三类xpath
            if rank is None:
                rank = tr.xpath('./td[1]/b/text()').extract_first()
                ent_name = tr.xpath('./td[2]/text()').extract_first()
                country = tr.xpath('./td[3]/text()').extract_first()

            # 第四类xpath
            if rank is None:
                rank = tr.xpath('./td[1]//text()').extract_first()
                ent_name = tr.xpath('./td[3]//text()').extract_first()
                country = tr.xpath('./td[4]/text()').extract_first()

            item = Fortune500Item(rank=rank, ent_name=ent_name, country=country, year=year)
            yield item
