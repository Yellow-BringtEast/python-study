import scrapy

from ..items import MeizituItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.jdlingyu.com']
    start_urls = ['https://www.jdlingyu.com/tuji/mzitu/page/1']

    page = 0

    def parse(self, response, **kwargs):
        a_list = response.xpath('//div[@class="post-info"]/h2/a')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            yield scrapy.Request(url=href, callback=self.parse_pic, meta={'name': name})

        if self.page < 5:
            self.page += 1
            url = f'https://www.jdlingyu.com/tuji/mzitu/page/{self.page}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_pic(self, response):
        name = response.meta['name']
        img_list = response.xpath('//div[@class="entry-content"]//img/@src')

        for img in img_list:
            src = img.extract()
            pic = MeizituItem(name=name, src=src)

            yield pic
