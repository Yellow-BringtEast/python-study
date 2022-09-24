import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="list-cont"]//span//span/text()')

        for name, price in zip(name_list, price_list):
            print(name.extract())
            print(price.extract())
