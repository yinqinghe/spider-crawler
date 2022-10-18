import scrapy
import pymysql
import scrapy
from scrapy import Request
from scrapy.selector import Selector

class WechatofficialpicsSpider(scrapy.Spider):
    name = 'wechatofficialPics'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ['http://mp.weixin.qq.com/']

    def start_requests(self):
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='sun',
        #                        charset='utf8')
        # # 创建游标
        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        # for i in range(0, 176):  # 176    100
        #     num = i * 10
        #     sql_query_id = f"select link from nanico where id between 1+{num} and 10+{num}"
        #     print(f"第{num}页")
        #     cursor.execute(sql_query_id)
        #     result = cursor.fetchall()  # 接收查询到的结果
        #     # print(result)
        #     print(len(result))
        #     for r in result:
        #         link = r['link']
        #         print(link)
        link = 'http://mp.weixin.qq.com/s?__biz=Mzg4OTcyNDY3OA==&mid=2247484198&idx=1&sn=44ea961445b5fb7f0bf781033eef3557&chksm=cfe6c94ff891405997d9f7144f7d28575a941aa5b6f8c0e6dbc6d3add8c32ecfb6bfe2bfa29b#rd'
        yield self.make_requests_from_url(link)

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, callback=self.parse)
    def parse(self, response):
        selector=Selector(response=response)
        img=selector.xpath('//img').getall()
        # img_src=selector.xpath('//img/').getall()
        # img_src=selector.re('<img data-height=".*?" data-ratio=".*?" data-src="(?P<src>.*?)" data-type=".*?" data-w=".*?" data-width=".*?">')
        # img_src=selector.re('<img data-height=".*?" data-ratio=".*?" data-src="(?P<datasrc>.*?)" data-type="jpeg" data-w="1000" data-width="1000">')
        img_src=selector.re('"https://mmbiz.qpic.cn/mmbiz_jpg/(?P<datasrc>.*?)"')
        for i in img_src:
            link='https://mmbiz.qpic.cn/mmbiz_jpg/'+i
            # link = response.urljoin(img_src[i])
            print(link)

        # print(img_src)
        # print(len(img_src))
        # print(img)
        # print(len(img))
        # print(response.text)
        pass
