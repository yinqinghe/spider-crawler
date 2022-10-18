import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import toutiao
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
import random
class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    start_urls = ['http://www.toutiao.com/']
    with open('D:\C#\python\爬虫\Scrapy\OldLearn\cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.readlines()
    # print(cookie[8])
    # print(len(cookie))
    # cookie = cookie.split('\n')[0]
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'cookie':'tt_webid=7081250641512121870; ttcid=84b17e80b7e341c4aae41e92d97d65ea36; s_v_web_id=verify_l29nfh0y_B5Acau7h_wXEr_4c98_9DkI_jHq7AndlRNji; local_city_cache=北京; csrftoken=b4b36a61f1f11a200cb8426558f3efcb; _tea_utm_cache_24=undefined; passport_csrf_token=3e05b9ccb777243cf9d3dd12d7e64295; passport_csrf_token_default=3e05b9ccb777243cf9d3dd12d7e64295; sso_uid_tt=1d7796fc0b298a3de158ba1fc0f60994; sso_uid_tt_ss=1d7796fc0b298a3de158ba1fc0f60994; toutiao_sso_user=df695d9843ca86a54f1d7b3caa7fe2d2; toutiao_sso_user_ss=df695d9843ca86a54f1d7b3caa7fe2d2; sid_ucp_sso_v1=1.0.0-KGMzNThjZGRlYWJkMDBkYWQ5OGJkOGYyNDFiYzY1MDRlYmM3MzJjZjcKEgiKqMTvWBCi4YeTBhgYOAhABRoCbGYiIGRmNjk1ZDk4NDNjYTg2YTU0ZjFkN2IzY2FhN2ZlMmQy; ssid_ucp_sso_v1=1.0.0-KGMzNThjZGRlYWJkMDBkYWQ5OGJkOGYyNDFiYzY1MDRlYmM3MzJjZjcKEgiKqMTvWBCi4YeTBhgYOAhABRoCbGYiIGRmNjk1ZDk4NDNjYTg2YTU0ZjFkN2IzY2FhN2ZlMmQy; odin_tt=8179021f346ccfb517dba879d6382786f16a72502b51983e2440bc3bebe5f646ad871673a1aeb8956cf85726b33f3950; sid_guard=df695d9843ca86a54f1d7b3caa7fe2d2|1650585762|5184000|Tue,+21-Jun-2022+00:02:42+GMT; uid_tt=1d7796fc0b298a3de158ba1fc0f60994; uid_tt_ss=1d7796fc0b298a3de158ba1fc0f60994; sid_tt=df695d9843ca86a54f1d7b3caa7fe2d2; sessionid=df695d9843ca86a54f1d7b3caa7fe2d2; sessionid_ss=df695d9843ca86a54f1d7b3caa7fe2d2; sid_ucp_v1=1.0.0-KGVkZDE5OTIxMDI0YjgwNjhmOTIxNWM5ZjlmOTcyZGJlZjE3N2FjZDYKFAiKqMTvWBCi4YeTBhgYIA44CEAFGgJsZiIgZGY2OTVkOTg0M2NhODZhNTRmMWQ3YjNjYWE3ZmUyZDI; ssid_ucp_v1=1.0.0-KGVkZDE5OTIxMDI0YjgwNjhmOTIxNWM5ZjlmOTcyZGJlZjE3N2FjZDYKFAiKqMTvWBCi4YeTBhgYIA44CEAFGgJsZiIgZGY2OTVkOTg0M2NhODZhNTRmMWQ3YjNjYWE3ZmUyZDI; tt_anti_token=mEBOVG1Rbmq9UKNH-b611ee2e00c51516b01e04ed1244d0a689a5f568568fe9d74ece64417258151d; ttwid=1|MJCfWonzOscnfKFlhveST6Oo46EA-dE99S1AFMqdkzc|1650589340|c73a74fbc9c84e774a8fdaa9951f584a883afdef9f8701f74ebcc5992fbaf370; MONITOR_WEB_ID=d1833ac6-3ef1-4d38-a5be-ba5e4fe2688d; tt_scid=3OAg2GFLUvO6aZ-KziD3b9Q3ak6LEZSnsU2Wr2tL0432vOshcAbPkZSUAeMuU2Oe821a',
    }

    # d = DesiredCapabilities.CHROME
    # d['goog:loggingPrefs'] = {'browser': 'ALL'}
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(desired_capabilities=d, chrome_options=options)
    #
    # # driver.get('http://www.baidu.com')
    # driver.get(url='http://127.0.0.1:8080/web%E4%BD%9C%E4%B8%9A4/toutiao%20.html')
    def start_requests(self):
        # url = 'https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_article&token=MS4wLjABAAAAzWKMSpUD00qeyjBtAm5-sIDbF2MCDpJD1C5EyzgAcSNs5Tot4WamsjJlPYOKtVYh&max_behot_time=1633655016739&aid=24&app_name=toutiao_web' \
        #       '&_signature=_02B4Z6wo0010134momQAAIDD.iRYJ50m9qd-AqbAAL33VMIalaAJqwUWu0aE3B5ffuXMCqvTQC80oyaQdDdRKWDNPtk0Ts6p0Jyj3WtMQEPBK7smL3m4IADO-uTysM53xblXTKsL1Oduaxmta7'              #1623168139463
        # url='https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_ugc&token=MS4wLjABAAAAZ4Hwu5YDysuwNnR85W69NIETIiucQctQRaxwxXneD18&max_behot_time=1649584858795&aid=24&app_name=toutiao_web' \
        #     '&_signature=_02B4Z6wo00f01OVZjVgAAIDAZVt3GZyBWyTldYnAAFs4JfVsd5FUCpvmphYubkNGqoUPxHOIsoAL7lrbdszN4AL1Ho2Swryvz-Xg2iAOHHVJ8vhBO7u7z1gS.R3IXYZeEAlyMkJW3gjQHt5l6c'

        url=input("请输入url:")
        yield self.make_requests_from_url(url)
        #1637201727723
    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True,callback=self.parse_kind_vedio,headers=self.header)
    def parse_kind_vedio(self, response):
        # https: // www.toutiao.com / api / pc / list / user / feed?category = profile_all & token = MS4wLjABAAAAqda3b7NbR78sh_RxCGg3HHkQCXwnjn0h2vSymkRAIn3RhDrYQVpKPeyRbwQlCokx & max_behot_time = 1648076171518 & aid = 24 & app_name = toutiao_web & _signature = _02B4Z6wo00d01NCLkVgAAIDAUIlrGO9VY6jQp7XAAFZK2C814nXCLTHguBCghvR - pU17AyFl8SL965oQAtnmeuy0tcOfTHtmJEOqJLwHXKHYrKdJB9UDAwiCR7jAv4HWqyIWUQ02ciDBNciqa1
        item = toutiao()
        res = json.loads(response.text)
        list = res['data']
        # print(list)
        print(len(list))
        for l in list:
            if l.get('read_count') is None and l.get('comment_base') is not None:
                # print(l)
                # for ll in l['comment_base']:
                #     print(ll)
                item['title'] = l['comment_base']['share']['share_title']
                item['link'] = l['comment_base']['share']['share_url']
                item['abstract'] = l['comment_base']['action']['digg_count']
                item['read_count'] = l['comment_base']['action']['read_count']
                item['comment_count'] = l['comment_base']['action']['comment_count']
                create_time = l['comment_base']['create_time']
                create_time = time.localtime(int(create_time))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
                publish_time = l['behot_time']
                publish_time = time.localtime(int(publish_time))
                item['publish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', publish_time)
                time1 = time.localtime(time.time())
                item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
                yield item
                continue
            if l.get('publish_time') is None:
                continue

            if l.get('content') is not None:
                item['title'] = l['content']
            elif l.get('title') is not None:
                item['title'] = l['title']

            if l.get('create_time') is None:
                behot_time = l['behot_time']
                behot_time = time.localtime(int(behot_time))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', behot_time)
            elif l.get('create_time') is not None:
                create_time = l['create_time']
                create_time = time.localtime(int(create_time))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', create_time)

            if l.get('action') is not None:
                item['link'] = l['share']['share_url']
                item['abstract'] = l['action']['digg_count']
                item['read_count'] = l['action']['read_count']
                item['comment_count'] = l['action']['comment_count']
            elif l.get('action') is None:
                item['link'] = l['share_url']
                item['abstract'] = l['digg_count']

                item['read_count'] = l['read_count']
                item['comment_count'] = l['comment_count']

            publish_time = l['publish_time']
            publish_time = time.localtime(int(publish_time))
            item['publish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', publish_time)
            time1 = time.localtime(time.time())
            item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(item)
            yield item
        max_behot_time = res['next']['max_behot_time']
        print(max_behot_time)

        # var i = { url: "https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAAEuWQJceClr0Ngb5pfgzlkJtMwCM2-bMxYHvRsO8z2nc&max_behot_time=" + max_time + "&aid=24&app_name=toutiao_web"}
        # var i = {url: "https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_ugc&token=MS4wLjABAAAA4v67UNE6D2FLWu8d70OJAVpNRJu5rikp7-3Hh5HI4J8&max_behot_time=" + max_time + "&aid=24&app_name=toutiao_web"}

        js = """
          function get_signature(max_time){
var i={url:"https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAAlI8KgH0CBJGovvEALpI4kA25QrGtKkXrz30LHMYCy20&max_behot_time="+max_time+"&aid=24&app_name=toutiao_web"}
                        var a=window.byted_acrawler;
                        console.log("是滴哦v考虑");
                        console.log(a);
                        console.log(i);
                        var r=a.sign;
                        console.log(r);
                        console.log(r.call(a,i));
                        console.log(i.url+'&_signature='+r.call(a,i))
                        return r.call(a,i);
                    }
                    var max_time='%d';
                    console.log(get_signature(max_time));
                    """ % (int(max_behot_time))
        self.driver.execute_script(js)  # 调用/执行js语句的方法
        list_br = self.driver.get_log("browser")
        # print(list)
        if len(list_br) == 10:
            url = list_br[7]['message'].split('"')[1]
            print(url)
        elif len(list_br) == 12:
            url = list_br[9]['message'].split('"')[1]
            print(url)
        if len(list) == 0 or len(list)==1:
            return 0
        yield self.make_requests_from_url(url)
        pass
    def parse_kind_today(self, response):
        item = toutiao()
        # print(res)
        res = json.loads(response.text)
        # print(res)
        list = res['data']
        # print(list)
        print(len(list))
        if len(list) == 0 or len(list)==1:
            return 0
        for l in list:
            # print()
            item['link'] = l['share_url']
            if l.get('content') is not None:
                # print(l)
                item['title'] = l['content']
                create_time = l['create_time']
                create_time = time.localtime(int(create_time))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
            elif l.get('title') is not None:
                item['title'] = l['title']
                behot_time = l['behot_time']
                behot_time = time.localtime(int(behot_time))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', behot_time)
                # continue
            item['abstract'] = l['digg_count']
            publish_time = l['publish_time']
            publish_time = time.localtime(int(publish_time))
            item['publish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', publish_time)

            item['read_count'] = l['read_count']
            item['comment_count'] = l['comment_count']

            time1 = time.localtime(time.time())
            item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(item)
            yield item
        max_behot_time = res['next']['max_behot_time']
        print(max_behot_time)
        # var i = { url: "https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAAEuWQJceClr0Ngb5pfgzlkJtMwCM2-bMxYHvRsO8z2nc&max_behot_time=" + max_time + "&aid=24&app_name=toutiao_web"}

        js = """
          var i={url:"https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAA4v67UNE6D2FLWu8d70OJAVpNRJu5rikp7-3Hh5HI4J8&max_behot_time="+max_time+"&aid=24&app_name=toutiao_web"}
          function get_signature(max_time){
                        var a=window.byted_acrawler;
                        console.log("是滴哦v考虑");
                        console.log(a);
                        console.log(i);
                        var r=a.sign;
                        console.log(r);
                        console.log(r.call(a,i));
                        console.log(i.url+'&_signature='+r.call(a,i))
                        return r.call(a,i);
                    }
                    var max_time='%d';
                    console.log(get_signature(max_time));
                    """ % (int(max_behot_time))
        self.driver.execute_script(js)  # 调用/执行js语句的方法
        list = self.driver.get_log("browser")
        # print(list)
        if len(list) == 10:
            url = list[7]['message'].split('"')[1]
            print(url)
        elif len(list) == 12:
            url = list[9]['message'].split('"')[1]
            print(url)

        yield self.make_requests_from_url(url)
        pass
    def parse_kind(self, response):
        item=toutiao()
        # print(res)
        res= json.loads(response.text)
        # print(res)
        list = res['data']
        # print(list)
        print(len(list))
        if len(list)==0:
           return 0
        for l in list:
            # print()
            item['link']=l['share_url']
            if l.get('rich_content') is None:
                # print(l)
                continue
                # item['title']='https://www.toutiao.com/w/1687305872745472/'
            item['title']=l['rich_content'].replace("<br>","")
            item['abstract']=l['digg_count']
            publish_time=l['publish_time']
            publish_time = time.localtime(int(publish_time))
            item['publish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', publish_time)
            create_time=l['create_time']
            create_time = time.localtime(int(create_time))
            item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
            item['read_count']=l['read_count']
            item['comment_count']=l['comment_count']

            time1 = time.localtime(time.time())
            item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(item)
            yield item
        max_behot_time=res['next']['max_behot_time']
        print(max_behot_time)
        #var i={url:"https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAA4v67UNE6D2FLWu8d70OJAVpNRJu5rikp7-3Hh5HI4J8&max_behot_time="+max_time+"&aid=24&app_name=toutiao_web"}


        js = """
        	function get_signature(max_time){
var i={url:"https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAAEuWQJceClr0Ngb5pfgzlkJtMwCM2-bMxYHvRsO8z2nc&max_behot_time="+max_time+"&aid=24&app_name=toutiao_web"}
        				var a=window.byted_acrawler;
        				console.log("是滴哦v考虑");
        				console.log(a);
        				console.log(i);
        				var r=a.sign;
        				console.log(r);
        				console.log(r.call(a,i));
        				console.log(i.url+'&_signature='+r.call(a,i))
        				return r.call(a,i);
        			}

                    var max_time='%d';

        			console.log(get_signature(max_time));
        			""" % (int(max_behot_time))
        self.driver.execute_script(js)  # 调用/执行js语句的方法
        list = self.driver.get_log("browser")
        # print(list)
        if len(list)==10:
            url = list[7]['message'].split('"')[1]
            print(url)
        elif len(list)==12:
            url = list[9]['message'].split('"')[1]
            print(url)
        # print(len(list))
        # print(list[9]['message'])
        # url = list[9]['message'].split('"')[1]
        # print(url)
        yield self.make_requests_from_url(url)
        pass
    def parse(self, response):
        item=toutiao()
        # print(res)
        res= json.loads(response.text)
        # print(res)
        list = res['data']
        # print(list)
        print(len(list))
        for l in list:
            # print()
            item['link']=l['article_url']
            item['title']=l['title']
            item['abstract']=l['abstract']
            publish_time=l['publish_time']
            publish_time = time.localtime(int(publish_time))
            item['publish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', publish_time)
            item['read_count']=l['read_count']
            item['comment_count']=l['comment_count']
            time1 = time.localtime(time.time())
            item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            # print(item)
            # yield item
        max_behot_time=res['next']['max_behot_time']
        print(max_behot_time)
        url = f'https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_article&token=MS4wLjABAAAAzWKMSpUD00qeyjBtAm5-sIDbF2MCDpJD1C5EyzgAcSNs5Tot4WamsjJlPYOKtVYh&max_behot_time={max_behot_time}&aid=24&app_name=toutiao_web&' \
              '_signature=_02B4Z6wo00901k7XUlQAAIDCztWoF0M8k35O81bAAPHmSileFxyeUsNCGpJ.M6vOjW1l4pS4-6mfU.4zLyrKP5m-OGCy60td4Y-AyTr7-FNDqk27tZvVb6-KUdQFZl843eicJVeE56NVHg5Fd6'

        print(url)
        # time.sleep(5)
        # yield self.make_requests_from_url(url)
        pass
