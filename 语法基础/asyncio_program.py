import time
import asyncio


# 单线程爬虫
def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('-')[-1])
    time.sleep(sleep_time)
    print('ok {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)


start = time.time()
main(['url-1', 'url-2', 'url-3', 'url-4'])
end = time.time()
t = end - start
print('execute time:', t)


# 异步接口写同步程序导致效率并没有提升
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('-')[-1])
    await asyncio.sleep(sleep_time)
    print('ok {}'.format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)


start = time.time()
asyncio.run(main(['url-1', 'url-2', 'url-3', 'url-4']))
end = time.time()
t = end - start
print('execute time:', t)


# 协程
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('-')[-1])
    await asyncio.sleep(sleep_time)
    print('ok {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task


start = time.time()
asyncio.run(main(['url-1', 'url-2', 'url-3', 'url-4']))
end = time.time()
t = end - start
print('execute time:', t)
