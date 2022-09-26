# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re

from .settings import PROXY_URL_FORMATTER

schema_pattern = re.compile(r'http|https$', re.I)
ip_pattern = re.compile(r'^([0-9]{1,3}.){3}[0-9]{1,3}$', re.I)
port_pattern = re.compile(r'^[0-9]{2,5}$', re.I)


class IpProxyPoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    schema = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    original = scrapy.Field()
    used_total = scrapy.Field()
    success_times = scrapy.Field()
    continuous_failed = scrapy.Field()
    created_time = scrapy.Field()

    # 检查IP代理的格式是否正确
    def _check_format(self):
        if self['schema'] is not None and self['ip'] is not None and self['port'] is not None:
            if schema_pattern.match(self['schema']) and ip_pattern.match(self['ip']) and port_pattern.match(
                    self['port']):
                return True
        return False

    # 获取IP代理的url
    def _get_url(self):
        return PROXY_URL_FORMATTER % {'schema': self['schema'], 'ip': self['ip'], 'port': self['port']}
