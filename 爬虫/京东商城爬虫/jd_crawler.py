import requests
from lxml import etree
from typing import Optional, List
import sqlite3
import random
import time

# 全局参数 - 消息头
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  'like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
}


class JDCrawler:
    """
    爬取京东搜索页面指定商品的sku、价格、商品名称，店铺名称及评论数，
    并存入sqlite3数据库中。
    """

    def __init__(self,
                 keyword: str = '潭酒',
                 init_page: int = 1,
                 total_page: int = 1,
                 header: Optional[dict] = None, ) -> None:
        """
        初始化参数，若需要爬取所有页面请勿修改init_page及total_page！
        直接调用run()方法开始爬取并保存数据。

        :param keyword:     爬虫爬取的关键词：默认为“潭酒”
        :param init_page:   网页的初始页码：默认为1
        :param total_page:  搜索的关键词总页码：默认为1
        :param header:      消息头
        """

        # 需爬取的信息
        url = 'https://search.jd.com/Search?keyword={}&page={}'
        attr_list = ['sku_id', 'sku_name', 'img_url', 'shop_name', 'sku_price', 'comment_count']

        # sqlite3连接器
        conn = sqlite3.connect('jd_crawler_data.sqlite')

        self._url = url
        self._keyword = keyword
        self._init_page = init_page
        self._init_url = url.format(self._keyword, 1)
        self._total_page = total_page
        self._attr_list = attr_list
        self._conn = conn

        if header is None:
            self._header = HEADER

    @property
    def keyword(self) -> str:
        """
        :return: 爬虫程序的关键词
        """
        return self._keyword

    @property
    def init_page(self) -> int:
        """
        :return: 爬虫程序的初始爬取页面的页码数
        """
        return self._init_page

    @property
    def url(self) -> str:
        """
        :return: 爬虫程序爬取的页面url
        """
        return self._init_url

    @property
    def total_page(self) -> int:
        """
        :return: 当前关键词在搜索页面的总页数
        """
        return self._total_page

    @property
    def header(self) -> dict:
        """
        :return: 消息头
        """
        return self._header

    @property
    def attr_list(self):
        """
        :return: 爬虫程序需爬取的关键字属性信息
        """
        return self._attr_list

    def get_url(self, keyword: Optional[str] = None, page: Optional[int] = None) -> str:
        """
        通过keyword及page获取需爬取的页面url

        :param keyword: 爬取的关键词
        :param page:    爬取的当前页码数
        :return:        当前的url地址
        """
        if keyword is None:
            keyword = self._keyword

        if page is None:
            page = self._init_page

        return self._url.format(keyword, page)

    def get_total_page(self) -> int:
        """
        获取当前关键词在搜索页面的总页码数，在total_page及init_page均为默认参数1的情况下，
        该方法会将self._total_page设置为关键词在搜索页面的总页码数。

        :return: 关键词在搜索页面的总页码数
        """
        resp = requests.get(url=self._init_url, headers=self._header).text
        html = etree.HTML(resp)

        # 京东搜索结果页面前30项目可以直接爬取，后30项为异步渲染，可以通过构造正确的页码来获取
        # 所以对总页码数需要乘以2
        total_page = int(html.xpath('//*[@id="J_topPage"]/span/i/text()')[0]) * 2

        if (self._total_page > 1) & (self._total_page > total_page):
            raise Exception('需爬取页码数{}，大于可爬取的总页码数{}'.format(self._total_page, total_page))
        elif self._total_page == 1:
            # 根据self._total_page是否为默认值，确定是否改变self._total_page的值
            self._total_page = total_page
        elif (self._total_page > 1) & (self._total_page <= total_page):
            total_page = self._total_page

        return total_page

    def get_attr(self, cur_url: Optional[str] = None) -> List:
        """
        爬取关键词在当前页面的所有属性值

        :param cur_url: 当前页面地址
        :return:        当前页面商品的属性值
        """

        # 创建存储爬取信息的列表
        sku_id = []
        sku_name = []
        img_url = []
        shop_name = []
        sku_price = []
        comment_count = []

        # 爬取信息与所在xpath的字典，comment_count需特殊处理
        attr_xpath = {
            'sku_id': '//*[@class="gl-warp clearfix"]/li/@data-sku',
            'sku_name': '//*[@class="gl-warp clearfix"]/li//*[@class="p-name p-name-type-2"]/a/em',
            'img_url': '//*[@class="gl-warp clearfix"]/li//*[@class="p-img"]/a/img/@data-lazy-img',
            'shop_name': '//*[@class="curr-shop hd-shopname"]/@title',
            'sku_price': '//*[@class="gl-warp clearfix"]/li//*[@class="p-price"]/strong/i/text()',
            'comment_count': ''
        }

        # 如果未传入当前页面的地址，使用默认的搜索地址
        if cur_url is None:
            cur_url = self._init_url

        # 解析页面，获取需爬取的各项属性值
        resp = requests.get(url=cur_url, headers=self._header).text
        html = etree.HTML(resp)

        for attr in self._attr_list:

            if attr == 'sku_id':
                sku_id.append(html.xpath(attr_xpath[attr]))

            # 处理sku_name文字被分段的问题
            if attr == 'sku_name':
                sku_nm = html.xpath(attr_xpath[attr])
                for e in sku_nm:
                    sku_name.append(str(e.xpath('string(.)')).replace('\t\n', ' '))

            if attr == 'img_url':
                img_url.append(['https:' + img for img in html.xpath(attr_xpath[attr])])

            if attr == 'shop_name':
                shop_name.append(html.xpath(attr_xpath[attr]))

            if attr == 'sku_price':
                sku_price.append(html.xpath(attr_xpath[attr]))

            # comment_count为页面渲染出来的，无法直接解析，通过京东数据接口直接获取所有sku_id的评论数
            if attr == 'comment_count':
                com_url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='
                for sku in sku_id[0]:
                    com_url += sku + ','

                comment_count = []
                comment_resp = requests.get(url=com_url, headers=self._header).json()

                for comment in comment_resp['CommentsCount']:
                    comment_count.append(comment['CommentCountStr'])

        # 保存为列表，方便后续存入sqlite数据库
        sku_info = [[s_id, name, img, shop, price, comment] for s_id, name, img, shop, price, comment
                    in zip(sku_id[0], sku_name, img_url[0], shop_name[0], sku_price[0], comment_count)]

        return sku_info

    def save_to_sqlite(self, data: List = None) -> None:
        """
        将爬取到的数据存入数据库

        :param data: 需入库的数据
        """

        if data is None:
            raise ValueError('未传入数据，无法保存')

        # 创建表
        sql = """
        create table if not exists jd_crawler_data (
                sku_id int,
                product_name sting,
                img_url string,
                shop_name string,
                sku_price decimal(18,2),
                sku_comment int,
                key_word string,
                create_time timestamp not null default (datetime('now','localtime'))
        )
        """
        self._conn.execute(sql)
        self._conn.commit()

        # 将数据插入数据库
        for i in range(len(data)):
            insert_sql = """
            insert into jd_crawler_data(sku_id, product_name, img_url, shop_name, sku_price, sku_comment, key_word)
                                 values({}, '{}', '{}', '{}', {}, '{}', '{}') 
            """.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], self._keyword)
            self._conn.execute(insert_sql)

    def run(self) -> None:
        """
        爬虫主程序
        """

        # 获取需要爬取的总页码数
        total_page = self.get_total_page()

        if self._init_page > self._total_page:
            raise Exception('初始页码数为{}，大于可爬取的总页面数{}!'.format(self._init_page, self._total_page))

        # 爬取页码上商品的信息
        for page in range(self._init_page, total_page + 1):
            # 爬取过程
            print('-' * 50)
            print('搜索词：{}，共{}页，第{}页爬取中...'.format(self._keyword,
                                                  (self._total_page - self._init_page + 1),
                                                  (page - self._init_page + 1)))
            url = self.get_url(page=page)
            sku_info = self.get_attr(cur_url=url)
            print('搜索词：{}，共{}页，第{}页爬取完成！'.format(self._keyword,
                                                 (self._total_page - self._init_page + 1),
                                                 (page - self._init_page + 1)))

            # 存储过程
            print('-' * 50)
            print('搜索词：{}，共{}页，第{}页数据存储中...'.format(self._keyword,
                                                    (self._total_page - self._init_page + 1),
                                                    (page - self._init_page + 1)))
            self.save_to_sqlite(sku_info)
            print('搜索词：{}，共{}页，第{}页数据存储完成！'.format(self._keyword,
                                                   (self._total_page - self._init_page + 1),
                                                   (page - self._init_page + 1)))

            time.sleep(random.uniform(0, 2))

        self._conn.commit()
        self._conn.close()
        print('-' * 50)
        print('数据保存完成，请前往数据库查看！')


if __name__ == '__main__':
    keyword_list = ['潭酒', 'Apple']
    for key_word in keyword_list:
        crawler = JDCrawler(keyword=key_word)
        crawler.run()
        time.sleep(5)
