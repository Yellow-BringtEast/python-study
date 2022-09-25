# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from urllib.request import urlretrieve
import os


class MeizituPipeline:
    def process_item(self, item, spider):

        if not os.path.exists(f"./pic/{item.get('name')}"):
            os.makedirs(f"./pic/{item.get('name')}")

        url = item.get('src')
        name = f"./pic/{item.get('name')}/{url.split('/')[-1]}"

        urlretrieve(url=url, filename=name)

        return item
