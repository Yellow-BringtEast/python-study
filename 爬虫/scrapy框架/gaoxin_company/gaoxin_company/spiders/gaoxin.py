import scrapy
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashResponse, SplashJsonResponse, SplashTextResponse, SplashRequest

from ..items import GaoxinCompanyItem


class GaoxinSpider(CrawlSpider):
    name = 'gaoxin'
    allowed_domains = ['www.innocom.gov.cn']
    start_urls = ['http://www.innocom.gov.cn/gqrdw/c101481/list_gsgg_l2.shtml']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@id="page_div"]'), process_request='use_splash',
             callback='parse_item', follow=False),
    )

    # 重写start_requests函数，将scrapy.Request替换为SplashRequest
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, args={'wait': 3})

    # process_request使用的函数
    def use_splash(self, request, response):
        request.meta['splash'] = {
            'endpoint': 'render.html',
            'args': {
                'wait': 3
            }
        }

    # 重写_requests_to_follow函数，将SplashResponse, SplashJsonResponse, SplashTextResponse加入类型检查中
    def _requests_to_follow(self, response):
        if not isinstance(response, (HtmlResponse, SplashResponse, SplashJsonResponse, SplashTextResponse)):
            return
        seen = set()
        for rule_index, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            for link in rule.process_links(links):
                seen.add(link)
                request = self._build_request(rule_index, link)
                yield rule.process_request(request, response)

    # 获取二级页面地址
    def parse_item(self, response):
        url_list = response.xpath('//ul[@class="list"]/li')

        for url in url_list:
            href = url.xpath('./a/@href').extract_first()
            href = 'http://www.innocom.gov.cn' + href

            yield scrapy.Request(url=href, callback=self.parse_download)

    # 获取需要下载的文件地址及文件名
    def parse_download(self, response):

        name = response.xpath('//div[@class="fjjian"]//a/text()').extract_first()
        url = response.xpath('//div[@class="fjjian"]//a/@href').extract_first()
        replace_str = response.url.split('/')[-1]
        url = response.url.replace(replace_str, '') + url

        file = GaoxinCompanyItem(file_url=url, file_name=name)
        yield file
