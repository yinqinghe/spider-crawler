import re
import time

import pymysql
import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import Picslink
class NanicopicsSpider(scrapy.Spider):
    name = 'nanicoPics'
    allowed_domains = ['t-nani.co.kr']
    start_urls = ['http://t-nani.co.kr//']

    def start_requests(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='sun',
                               charset='utf8')
        # 创建游标
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        for i in range(0,176):  #176    100
            num=i*10
            sql_query_id = f"select link from nanico where id between 1+{num} and 10+{num}"
            print(f"第{num}页")
            cursor.execute(sql_query_id)
            result = cursor.fetchall()  # 接收查询到的结果
            # print(result)
            print(len(result))
            for r in result:
                link=r['link']
                print(link)
        # link = 'http://t-nani.co.kr/shop/shopdetail.html?branduid=1980200&xcode=007&mcode=003&scode=&type=Y&sort=order&cur_code=007&GfDT=amV%2FWA%3D%3D'
                yield self.make_requests_from_url(link)


    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, callback=self.parse)
    def parse(self, response):
        selector=Selector(response=response)
        # print(response.text)
        pics=Picslink()
        img=selector.xpath('//img/@src').getall()
        title=selector.xpath('//div[@class="tb-left"]/text()').getall()
        # title=title.xpath('.//div[@class="tb-left"]')
        print(title[0].strip())
        pics['title']=title[0].strip()
        time1 = time.localtime(time.time())
        t = time.strftime('%Y-%m-%d %H:%M:%S', time1)
        pics['nowtime'] = t
        ro=re.compile('http://gi.esmplus.com/.*?')
        xl=re.compile('http://t-nani.co.kr/shopimages/xlsksl1018/.*?')
        i=1
        for r in range(0,len(img)):
            url=response.urljoin(img[r])
            roer=ro.search(url)
            xlsk=xl.search(url)
            print(url)
            if roer!=None :
                # print("匹配到了roer")
                pics[f'link{i}']=url
                i=i+1
                print(url)
                # name_apl=url.split('/')[-1]
                # pics['imgname']='孙允珠'+name_apl
                # print(name_apl)
                # print(pics)
                # yield pics
            elif xlsk!=None:
                # print(xlsk)
                pics[f'link{i}']=url
                i=i+1
                print(url)
                # name_num=url.split('/')[-1].split('?')[0]
                # pics['imgname']='孙允珠'+name_num
                # print(name_num)
                # yield pics
        # print(pics)
        # print(len(pics))
        while len(pics) != 62:
            pics[f'link{i}']=''
            i=i+1
        # print(len(pics))
        # print(pics)
        yield pics
            # print(url)
        # print(img)
        print(len(img))
        pass
