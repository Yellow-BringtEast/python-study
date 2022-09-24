# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymysql import connect

# 加载settings文件
from scrapy.utils.project import get_project_settings


class DushuPipeline:
    def process_item(self, item, spider):
        return item


class MysqlPipeline:
    def __init__(self):
        self.cur = None

        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.con = connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )

    def open_spider(self, spider):
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        # 插入数据
        sql = f'''
        insert into xc_data.dushuwang(name, pic) values('{item['name']}', '{item['pic']}')
        '''
        self.cur.execute(sql)

        # 提交数据
        self.con.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.con.close()
