import json
import time

import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import PIPIXIA

class PipixiaSpider(scrapy.Spider):
    name = 'pipixia'
    allowed_domains = ['i.snssdk.com']
    start_urls = ['http://i.snssdk.com/']
    i=0
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'cookie': 'install_id=233538660889533; ttreq=1$ebb60504d307c8b05fb9d63cfb0025bf150088ca; passport_csrf_token_default=2c9595bd2132f836482e37eb83b6e35b; d_ticket=0d04a68d45b9351c392cf9cf53ef98a4d5f34; odin_tt=3060bb006e5ad801df771895551db7d677c268655e05d59d837dfef292ad16c59e92c3311991b59c45bb26c9513fde3019ef7a42911e725fe9583349ee59ba97e7cd0e99f11cff73a4425386062a2f85; n_mh=di2ji2lzfrBFqSRT6WZJg3yamijiXDGKL5wUXulQYmU; sid_guard=674688ea7075114198f512272a6bfc54%7C1651461884%7C5184000%7CFri%2C+01-Jul-2022+03%3A24%3A44+GMT; uid_tt=5d36ec24aa1252816197fcf8d016238f; sid_tt=674688ea7075114198f512272a6bfc54; sessionid=674688ea7075114198f512272a6bfc54',

    }
    def start_requests(self):
        # url = 'https://i.snssdk.com/bds/user/publish_list/?api_version=1&cursor=1609714494423429&feed_count=1&list_type=contributions&user_id=62805304892&direction=2&iid=4244556027555640&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=161&version_name=1.6.1&device_platform=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&uuid=2573272117428052&openudid=4b255db2a972088f&manifest_version_code=161&resolution=900*1600&dpi=320&update_version_code=1611&_rticket=1651206661768&ts=1651206661&as=a22696863540626acb2822&cp=6208206d51b764a6e2]kKo&mas=00dfd9c1845dbaa983a2dd0b3250343f297373237379f9b9537353'
        #1648478715726541
        # url = 'https://i.snssdk.com/bds/user/favorite/?api_version=4.2&cursor=0&layout_style=1&feed_count=0&vrsr_enable=1&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651463517502&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651463517'
        # url = 'https://i.snssdk.com/bds/user/favorite/?api_version=4.2&cursor=0&layout_style=1&feed_count=1&vrsr_enable=1&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651463517502&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651463517'
        # url = 'https://i.snssdk.com/bds/ward/list/?layout_style=1&feed_count=0&api_version=4.2&cursor=0&vrsr_enable=1&user_id=2651638450357517&list_type=userwards&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651465144572&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651465144'

        # url = 'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=0&cursor=0&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651465144595&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651465144'
        url = f'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=1&cursor=0&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=900*1600&dpi=320&update_version_code=40550&_rticket=1651473772506&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651473772'


        yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True,callback=self.parse,headers=self.header)
    def parse(self, response):
        res = json.loads(response.text)
        pipixia=PIPIXIA()
        data = res['data']['data']
        for d in data:
            if d.get('item') is None:
                # print(json.dumps(d, indent=2))
                # for i  in d:
                #     print(i)
                pipixia['title'] = d['comment_info']['share']['title']
                create_time = d['display_time']
                create_time = time.localtime(int(create_time))
                pipixia['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
                pipixia['share_url'] = d['comment_info']['share']['share_url']
                time1 = time.localtime(time.time())
                pipixia['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
                pipixia['vedio'] = 'null'

                yield pipixia
                continue
                # print(d)
            if d['item'].get('origin_video_download') is None:
                # print(d)
                continue
            pipixia['vedio'] = d['item']['origin_video_download']['url_list'][0]['url']

            pipixia['title'] = d['item']['content']
            create_time = d['item']['create_time']
            create_time = time.localtime(int(create_time))
            pipixia['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
            pipixia['share_url']=d['item']['share']['share_url']
            time1 = time.localtime(time.time())
            pipixia['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(pipixia)
            yield pipixia
        # print(data)
        cursor = res['data']['cursor']['loadmore_cursor']
        print(cursor)
        print(len(data))
        self.i=self.i+1
        ti=int(time.time())
        # time.sleep(5)
        # url = f'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=0&cursor={cursor}&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651465144595&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651465144'

        # url = f'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=0&cursor={cursor}&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket={str(ti) + "158"}&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts={ti}'
        url = f'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=1&cursor={cursor}&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=900*1600&dpi=320&update_version_code=40550&_rticket=1651473772506&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651473772'

        # url = f'https://i.snssdk.com/bds/ward/list/?layout_style=1&feed_count=0&api_version=4.2&cursor={cursor}&vrsr_enable=1&user_id=2651638450357517&list_type=userwards&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket={str(ti) + "108"}&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts={ti}'

        # url = f'https://i.snssdk.com/bds/user/favorite/?api_version=4.2&cursor={cursor}&layout_style=1&feed_count=2&vrsr_enable=1&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=900*1600&dpi=320&update_version_code=40550&_rticket={str(ti) + "108"}&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts={ti}'

        # url = f'https://i.snssdk.com/bds/user/favorite/?api_version=4.2&cursor={cursor}&layout_style=1&feed_count={self.i}&vrsr_enable=1&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket={str(ti)+"108"}&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts={ti}'
        print(url)
        if len(data)==0:
            return
        yield self.make_requests_from_url(url)
        pass
