"""
异步爬虫
"""

import requests
from lxml import etree
import asyncio
import aiohttp  # 异步请求库
import time


# 地址、请求头
page_url = 'https://movie.douban.com/cinema/later/beijing/'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
    }

# 图片保存路径
file_path = './电影海报/'


# 请求页面信息获取电影海报地址 - 默认参数为可变对象是应该按以下方式处理
def get_photo_urls(urls=page_url, headers=None):
    if headers is None:
        headers = header
    html = requests.get(url=urls, headers=headers).text
    html = etree.HTML(html)
    photo_urls = html.xpath('//*[@class="thumb"]/img/@src')

    return photo_urls


# 异步请求页面内容 - 固定写法
async def fetch_content(photo_url):
    async with aiohttp.ClientSession(
        headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(photo_url) as response:
            return await response.read(), photo_url.split('/')[-1]


# 主函数入口
async def main():
    photo_urls = get_photo_urls()
    tasks = [fetch_content(url) for url in photo_urls]
    images = await asyncio.gather(*tasks)

    for img, path in images:
        photo_path = file_path + path
        with open(photo_path, 'wb') as f:
            f.write(img)


start = time.time()
asyncio.run(main())
end = time.time()
print('execute time:', end - start)
