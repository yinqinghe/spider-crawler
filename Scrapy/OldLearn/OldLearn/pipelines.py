# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import os.path
import re
import MySQLdb
import pymysql
import pymysql.cursors
# useful for handling different item types with a single interface
import scrapy
import requests
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
class ImgsPipLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        # print(item)
        title=item['title']
        title=re.sub('[*]','',title)
        if not os.path.exists(rf"D:\Pics\nanio\{title}"):
            os.makedirs(rf"D:\Pics\nanio\{title}")
        with open(rf"D:\Pics\nanio\{title}\{item['imgname']}",mode='wb') as f:
            f.write(requests.get(url=item['imgsrc']).content)
        # yield Request(url=item['imgsrc'],meta={'item':item},dont_filter=False)

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     items=request.meta['item']
    #     # print(request)
    #     # print(items)
    #     print(item)
    #     filepaths=item['imgname']
    #     filepath=f'full/{filepaths}'
    #     # print(filepath)
    #     image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
    #     # return f'full/{filepaths}.jpg'
    #     return f'full11/{filepaths}'
    #     # return filepath
    def item_completed(self, results, item, info):
        # print(item)
        # print(results)
        # print(item)
        return item

class OldlearnPipeline:
    def process_item(self, item, spider):
        print(item)
        return item

class MySQLPipeline:
    def __init__(self):
        # db='sun'
        # db='baidupics'
        # db='website_of_kind'
        # db='wechat'
        db='pipixia'

        host ='127.0.0.1'
        port = 3306
        user = 'root'
        passwd = '123456'
        self.db_conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset='utf8mb4')

        self.db_cur=self.db_conn.cursor()
    def process_item(self,item,spider):
        # self.insert_db_nanicopics(item)
        # self.insert_db_baijiahao(item)
        self.insert_db_pipixia_users(item)

        return item
    def insert_db_pipixia_users(self,item):
        values=(item['id_str'],
                item['name'],
                item['followers_count'],
                item['followings_count'],
                item['like_count'],
                item['description'])
        sql_add = "insert into users(id_str,name,followers_count,followings_count,like_count,description) values (%s,%s,%s,%s,%s,%s)"
        self.db_cur.execute(sql_add,values)
    def insert_db_pipixia(self,item):
        values=(item['vedio'],
                item['title'],
                item['create_time'],
                item['share_url'],
                item['nowtime'])
        sql_add = "insert into 美女身材精选(vedio,title,create_time,share_url,nowtime) values (%s,%s,%s,%s,%s)"
        self.db_cur.execute(sql_add,values)
    def insert_db_toutiao(self,item):
        values=(item['title'],
                item['link'],
                item['abstract'],
                item['publish_time'],
                item['read_count'],
                item['comment_count'],
                item['nowtime'],
                item['createtime'])
        sql_add = "insert into 自在糖飘飘(title,link,digg_count,publish_time,read_count,comment_count,nowtime,createtime) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.db_cur.execute(sql_add,values)

    def insert_db_baijiahao(self, item):
        values = (item['title'],
                  item['link'],
                  item['createtime'],
                  item['subtitle'],
                  item['article_id'],
                  item['publishtime'],
                  item['updatetime'],
                  item['dynamic_ctime'],
                  item['type'],
                  item['nowtime'],
                  item['itemtype'])
        sql_add = "insert into 小小时尚女神(title,link,createtime,subtitle,article_id,publishtime,updatetime,dynamic_ctime,type,nowtime,itemtype)" \
                  " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.db_cur.execute(sql_add, values)

    def insert_db_nanicopics(self,item):
        values=(item['title'],item['nowtime'],item['link1'],item['link2'],item['link3'],item['link4'],item['link5'],
                item['link6'],item['link7'],item['link8'],item['link9'],item['link10'],item['link11'],item['link12'],
                item['link13'],item['link14'],item['link15'],item['link16'],item['link17'],item['link18'],item['link19'],
                item['link20'],item['link21'],item['link22'],item['link23'],item['link24'],item['link25'],item['link26'],
                item['link27'],item['link28'],item['link29'],item['link30'],item['link31'],item['link32'],item['link33'],
                item['link34'],item['link35'],item['link36'],item['link37'],item['link38'],item['link39'],item['link40'],
                item['link41'],item['link42'],item['link43'],item['link44'],item['link45'],item['link46'],item['link47'],
                item['link48'],item['link49'],item['link50'],item['link51'],item['link52'],item['link53'],item['link54'],
                item['link55'],item['link56'],item['link57'],item['link58'],item['link59'],item['link60']
)
        # sql_add = "insert into nanicopics(title,link,create_time,aid,update_time,nowtime) values (%s,%s,%s,%s,%s,%s)"
        sql_add = "insert into nanicopics1(title,nowtime,link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,link28,link29,link30,link31,link32,link33,link34,link35,link36,link37,link38,link39,link40,link41,link42,link43,link44,link45,link46,link47,link48,link49,link50,link51,link52,link53,link54,link55,link56,link57,link58,link59,link60)" \
                  " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        self.db_cur.execute(sql_add,values)
    def insert_db_wechat(self,item):
        values=(item['title'],
                item['link'],
                item['create_time'],
                item['aid'],
                item['update_time'],
                item['nowtime'])
        sql_add = "insert into 孙允珠定拍1(title,link,create_time,aid,update_time,nowtime) values (%s,%s,%s,%s,%s,%s)"
        self.db_cur.execute(sql_add,values)


    def insert_db_baidupage(self,item):
        values=(item['title'],
                item['link'],
                item['nowtime'])
        sql_add = "insert into tiebapage_道晖芝吧_good(title,link,nowtime) values (%s,%s,%s)"
        self.db_cur.execute(sql_add,values)


    def insert_db_nanico(self,item):
        values=(item['title'],
                item['link'],
                item['pic'],
                item['price'])
        sql_add = "insert into nanico(title,link,Pic,price) values (%s,%s,%s,%s)"
        self.db_cur.execute(sql_add,values)

    def close_spider(self,spider):
        self.db_conn.commit()
        self.db_cur.close()
        self.db_conn.close()
