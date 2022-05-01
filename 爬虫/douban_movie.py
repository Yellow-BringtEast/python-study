"""
同步爬虫
"""

import requests
from lxml import etree
import time

# 地址、请求头
url = 'https://movie.douban.com/cinema/later/beijing/'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
    }

# 图片保存路径
file_path = './电影海报/'


# 请求页面信息获取电影海报地址
def get_photo_urls(urls=url, headers=None):
    if headers is None:
        headers = header
    html = requests.get(url=urls, headers=headers).text
    html = etree.HTML(html)
    photo_urls = html.xpath('//*[@class="thumb"]/img/@src')

    return photo_urls


# 保存海报
def save_photos(photo_urls, headers=None, path=file_path):
    if headers is None:
        headers = header

    for photo_url in photo_urls:
        img = requests.get(url=photo_url, headers=headers).content
        photo_path = path + photo_url.split('/')[-1]
        with open(photo_path, 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    start = time.time()

    # 获取海报连接
    photo_url_list = get_photo_urls()

    # 保存海报
    save_photos(photo_url_list)

    end = time.time()
    print('execute time:', end - start)

