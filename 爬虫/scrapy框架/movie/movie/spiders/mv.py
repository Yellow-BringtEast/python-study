import scrapy

from ..items import MovieItem


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    page = 0

    # 爬取第一个页面的名称及其对应的第二页的图片
    def parse(self, response, **kwargs):
        # 获取电影名称及其明细页面url对应的a标签
        a_list = response.xpath('//div[@class="co_content8"]//b/a[2]')

        for a in a_list:
            # 电影名称
            name = a.xpath('./text()').extract_first()
            # 明细页面url
            href = a.xpath('./@href').extract_first()
            url = 'https://www.ygdy8.net' + href

            # 对明细页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_pic, meta={'name': name})

        if self.page < 7:
            self.page += 1
            url = f'https://www.ygdy8.net/html/gndy/china/list_4_{self.page}.html'
            yield scrapy.Request(url=url, callback=self.parse)

    # 明细页电影海报获取
    def parse_pic(self, response):
        # 请求传入的meta参数
        name = response.meta['name']

        # 获取海报地址
        pic = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()

        # 生成item
        movie = MovieItem(name=name, pic=pic)

        # 将item返回给管道
        yield movie
