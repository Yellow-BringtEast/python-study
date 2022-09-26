# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from .utils import logger
import random


# 随机选择 IP 代理下载器中间件
class RandomProxyMiddleware(object):

    # 从 settings 的 PROXIES 列表中随机选择一个作为代理
    def process_request(self, request, spider):
        proxy = random.choice(spider.settings['PROXIES'])
        request.meta['proxy'] = proxy
        return None


# 随机选择 User-Agent 的下载器中间件
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 从 settings 的 USER_AGENTS 列表中随机选择一个作为 User-Agent
        user_agent = random.choice(spider.settings['USER_AGENT_LIST'])
        request.headers['User-Agent'] = user_agent
        return None

    def process_response(self, request, response, spider):
        # 验证 User-Agent 设置是否生效
        logger.info("headers ::> User-Agent = " + str(request.headers['User-Agent'], encoding="utf8"))
        return response
