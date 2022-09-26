import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import time
from ..utils import strip, logger
from ..items import IpProxyPoolItem


class ProxyPoolSpider(CrawlSpider):
    name = 'proxy_pool'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    rules = (
        Rule(LinkExtractor(allow=r'/free/inha/\d+/'), callback='parse', follow=True),
    )

    def parse(self, response, **kwargs):
        logger.info('正在爬取：< ' + response.request.url + ' >')

        tr_list = response.xpath('//tbody/tr')
        for tr in tr_list:
            ip = tr.xpath('./td[@data-title="IP"]/text()').extract_first()
            port = tr.xpath('./td[@data-title="PORT"]/text()').extract_first()
            schema = tr.xpath('./td[@data-title="类型"]/text()').extract_first()

            if schema.lower() == "http" or schema.lower() == "https":
                item = IpProxyPoolItem()
                item['schema'] = strip(schema).lower()
                item['ip'] = strip(ip)
                item['port'] = strip(port)
                item['original'] = '快代理'
                item['created_time'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))

                if item._check_format():
                    yield item
