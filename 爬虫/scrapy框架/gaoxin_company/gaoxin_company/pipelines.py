# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import scrapy


# 让pipeline继承FilesPipeline进行文件下载
class GaoxinCompanyPipeline(FilesPipeline):

    # 重写get_media_requests函数，将item.file_url传递给scrapy.Request，同时将item.file_name传递给meta
    # 以重写命名保存的文件
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['file_url'], meta={'title': item['file_name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        title = request.meta['title']
        return title
