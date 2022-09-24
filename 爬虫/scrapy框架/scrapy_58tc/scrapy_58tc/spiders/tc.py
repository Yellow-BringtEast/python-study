import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['cd.58.com']
    start_urls = ['https://cd.58.com/']

    def parse(self, response):
        # 网页源码字符串
        # content = response.text
        # print('=============================')
        # print(content)

        # 二进制数据
        body = response.body
        print('=============================')
        print(body)
