import json
import time
import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import Wechat_account
class WechatofficialSpider(scrapy.Spider):
    name = 'wechatofficial'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ['http://mp.weixin.qq.com/']
    with open('D:\C#\python\爬虫\课外学习\网站资源探索\微信公众号\cookie2.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    # random.seed(time.time())
    cookie = cookie.split('\n')[0]
    header = {
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'cookie': cookie,
    }
    def start_requests(self):
        for i in range(0,1):    #
            num=i*5
            url = f'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MzkwNjMyOTA2Mw==&type=9&query=&token=1009187860&lang=zh_CN&f=json&ajax=1'

            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True,callback=self.parse,headers=self.header)
    def parse(self, response):
        # selector=Selector(response=response)
        item=Wechat_account()

        res=json.loads(response.text)
        app_msg_list = res['app_msg_list']
        print(len(app_msg_list))
        for a in app_msg_list:
            ti = a['create_time']
            time1 = time.localtime(ti)
            t = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(t)
            update = a['update_time']
            time2 = time.localtime(update)
            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time2)
            time_n = time.localtime(time.time())
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time_n)
            item['nowtime']=nowtime
            item['create_time']=t
            item['link'] = a['link']
            item['title'] = a['title']
            item['aid'] = a['aid']
            item['update_time']=update_time
            # yield item
            # print(title)
            # print(link)
            print(item)
        pass
