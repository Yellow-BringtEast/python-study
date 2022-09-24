import scrapy

from ..items import DangdangItem


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['https://category.dangdang.com/cp01.01.02.00.00.00.html']

    # 页码
    page = 1

    def parse(self, response):
        # src = //ul[@class="bigimg"]/li/a/img/@data-original
        # name = //ul[@class="bigimg"]/li/a/img/@alt
        # price = //ul[@class="bigimg"]/li/p[@class="price"]/span[1]/text()

        # 获取所有需爬取数据相同xpath节点
        li_list = response.xpath('//ul[@class="bigimg"]/li')

        # 获取需要爬取的数据
        for li in li_list:
            src = li.xpath('./a/img/@data-original').extract_first()

            # 由于图片懒加载，第一本书的图片地址与其他图片地址xpath路径有差异，需判断处理
            if src:
                src = src
            else:
                src = li.xpath('./a/img/@src').extract_first()

            name = li.xpath('./a/img/@alt').extract_first()
            price = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()

            book = DangdangItem(src=src, name=name, price=price)

            # 获取一个book, 就将book交给pipelines
            yield book

        if self.page < 100:
            self.page += 1

            # 每页对应的url
            url = f'https://category.dangdang.com/pg{self.page}-cp01.01.02.00.00.00.html'

            # Request就是scrapy的get请求，callback就是你要执行的函数
            yield scrapy.Request(url=url, callback=self.parse)
