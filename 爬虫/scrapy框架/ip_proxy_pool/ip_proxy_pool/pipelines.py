# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import redis
from .settings import REDIS_HOST, REDIS_PORT, PROXIES_UNCHECKED_LIST, PROXIES_UNCHECKED_SET

server = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class IpProxyPoolPipeline:

    # 将可用的IP代理添加到代理池队列
    def process_item(self, item, spider):
        if not self._is_existed(item):
            server.rpush(PROXIES_UNCHECKED_LIST, json.dumps(dict(item), ensure_ascii=False))

    # 检查IP代理是否已经存在
    def _is_existed(self, item):
        added = server.sadd(PROXIES_UNCHECKED_SET, item._get_url())
        return added == 0
