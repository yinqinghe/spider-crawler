import json
import time

import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import PIPIXIA_USERS

class PipixiaUserSpider(scrapy.Spider):
    name = 'pipixia_user'
    allowed_domains = ['i.snssdk.com']
    start_urls = ['http://i.snssdk.com/']


    def start_requests(self):
        # url = 'https://i.snssdk.com/bds/user/publish_list/?api_version=1&cursor=1609714494423429&feed_count=1&list_type=contributions&user_id=62805304892&direction=2&iid=4244556027555640&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=161&version_name=1.6.1&device_platform=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&uuid=2573272117428052&openudid=4b255db2a972088f&manifest_version_code=161&resolution=900*1600&dpi=320&update_version_code=1611&_rticket=1651206661768&ts=1651206661&as=a22696863540626acb2822&cp=6208206d51b764a6e2]kKo&mas=00dfd9c1845dbaa983a2dd0b3250343f297373237379f9b9537353'
        #1648478715726541
        # url = 'https://i.snssdk.com/bds/user/favorite/?api_version=4.2&cursor=0&layout_style=1&feed_count=0&vrsr_enable=1&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651463517502&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651463517'
        # url = 'https://i.snssdk.com/bds/user/favorite/?api_version=4.2&cursor=0&layout_style=1&feed_count=1&vrsr_enable=1&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651463517502&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651463517'
        # url = 'https://i.snssdk.com/bds/ward/list/?layout_style=1&feed_count=0&api_version=4.2&cursor=0&vrsr_enable=1&user_id=2651638450357517&list_type=userwards&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651465144572&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651465144'

        # url = 'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=0&cursor=0&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651465144595&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651465144'
        # url = f'https://i.snssdk.com/bds/user/publish_list/?api_version=4.2&layout_style=1&feed_count=1&cursor=0&vrsr_enable=1&user_id=5807896266&list_type=contributions&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=900*1600&dpi=320&update_version_code=40550&_rticket=1651473772506&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651473772'

        # url='https://i.snssdk.com/bds/user/following/?cursor=1641369440389&count=50&user_id=2651638450357517&order_by=0&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket=1651465392887&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651465392'
        url='https://i.snssdk.com/bds/user/following/?cursor=0&count=50&user_id=2651638450357517&order_by=0&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=900*1600&dpi=320&update_version_code=40550&_rticket=1651476911155&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651476911'
        yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True,callback=self.parse)
    def parse(self, response):
        res = json.loads(response.text)
        pipixia=PIPIXIA_USERS()
        users = res['data']['users']
        print(len(users))
        for u in users:
            pipixia['id_str']=u['id_str']
            pipixia['name']=u['name']
            pipixia['followers_count']=u['followers_count']
            pipixia['followings_count']=u['followings_count']
            pipixia['like_count']=u['like_count']
            pipixia['description']=u['description']
            print(pipixia)
            yield pipixia

        cursor = res['data']['cursor']['loadmore_cursor']
        print(cursor)
        ti=int(time.time())
        if len(users)==0:
            return
        # url=f'https://i.snssdk.com/bds/user/following/?cursor={cursor}&count=50&user_id=2651638450357517&order_by=0&direction=1&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=1600*900&dpi=320&update_version_code=40550&_rticket={str(ti)+"887"}&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts={ti}'
        url=f'https://i.snssdk.com/bds/user/following/?cursor={cursor}&count=50&user_id=2651638450357517&order_by=0&direction=2&iid=233538660889533&device_id=2573272117428052&ac=wifi&channel=tengxun&aid=1319&app_name=super&version_code=405&version_name=4.0.5&device_platform=android&os=android&ssmix=a&device_type=SM-G9810&device_brand=samsung&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=405&resolution=900*1600&dpi=320&update_version_code=40550&_rticket=1651476911155&cdid=83b43c57-c003-4dc4-ab3c-6f258a8b5f5c&app_region=CN&sys_region=CN&time_zone=Asia%2FShanghai&carrier_region=CN&app_language=ZH&last_channel&recommend_disable=0&last_update_version_code=0&ts=1651476911'
        yield self.make_requests_from_url(url)

        pass
