# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request


# 如果想使用管道，就需要在settings中开启管道
class DangdangPipeline:
    def __init__(self):
        self.fp = None

    # 在爬虫开始前执行的一个Scrapy内置函数
    def open_spider(self, spider):
        # 打开文件
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 写入数据
        self.fp.write(str(item))

        return item

    # 在爬虫结束前执行的一个Scrapy内置函数
    def close_spider(self, spider):
        # 保存并关闭文件
        self.fp.close()


# 多条管道同时开启 - 需在settings中开启
# 下载图片
class DangdangDownloadPipeline:
    def process_item(self, item, spider):
        # 获取图片地址及名称
        url = 'http:' + item.get('src')
        name = './book/' + item.get('name').replace('*', '') + '.jpg'

        # 下载图片
        urllib.request.urlretrieve(url=url, filename=name)

        return item
