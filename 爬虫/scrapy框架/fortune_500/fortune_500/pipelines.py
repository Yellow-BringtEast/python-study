# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Fortune500Pipeline:
    def open_spider(self, spider):
        self.f = open('key.txt', 'w')

    def process_item(self, item, spider):

        if item['country'] is not None:
            item['country'] = "".join(item['country'].split())

        if item['ent_name'] is not None:
            item['ent_name'] = "".join(item['ent_name'].split())

        if item['country'] is None or item['country'] == '':
            pass
        elif ',' in item['country']:
            pass
        else:
            self.f.write(str(item))

        return item

    def close_spider(self, spider):
        self.f.close()
