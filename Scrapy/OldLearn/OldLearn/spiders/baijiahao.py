import re

import scrapy
from scrapy import Request
from scrapy.selector import Selector
import json
import time
from ..items import Baijiahao

class BaijiahaoSpider(scrapy.Spider):
    name = 'baijiahao'
    allowed_domains = ['baijiahao.baidu.com']
    start_urls = ['http://baijiahao.baidu.com/']
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'cookie': 'BIDUPSID=8F10C06B4F3326FE2876D959A11FB138; PSTM=1602322183; __yjs_duid=1_905405d7cc47199ebc65346ca416028b1617943503562; BDUSS=F3MjA1cXdWR1BweVBTa0tsdDhEd0pUTzVoSDlTd1BvMnlTZllQflFWZ2RWb3RoRVFBQUFBJCQAAAAAAQAAAAEAAABsYCsey97J4cnPv87Jz7~OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3JY2EdyWNhMW; BDUSS_BFESS=F3MjA1cXdWR1BweVBTa0tsdDhEd0pUTzVoSDlTd1BvMnlTZllQflFWZ2RWb3RoRVFBQUFBJCQAAAAAAQAAAAEAAABsYCsey97J4cnPv87Jz7~OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3JY2EdyWNhMW; x-logic-no=1; H_WISE_SIDS=110085_127969_132549_176399_179346_184716_188743_189755_190616_191254_194085_194511_194519_194530_195343_196426_197241_197711_197958_199568_200993_201193_201541_201701_202651_203190_203309_203520_204254_204305_204536_204778_204864_204917_205217_205234_205548_205569_206008_206122_206144_206249_206516_206681_206767_206905_207021_207177_207265_207364_207389_207471_207498_207610_207626_207716_207863_208001_208045_208055_208114_208163_208165_208225_208267_208271_208309_208312_208363_208559_208599_208721_208770_208772_208776_209140_209148_209294; BDSFRCVID=G7-OJexroG0xFB3D_Hm8uRtLxzTnskcTDYrEOwXPsp3LGJLVguQPEG0PttE_sDu-ox3logKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oCPbtDvDqTrP-trf5DCShUFsKq3dB2Q-XPoO3KJWsl_RQhn1LnI00lOrhnTnaj7W3Mbgy4op8P3y0bb2DUA1y4vpKbQILgTxoUJ2bp5rqpbGqtnWDPAebPRih4r9QgbtBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PO5pCX5-CsWIJT2hcHMPoosIJ9QxK5Qh4nLp6tQJ3rMgc-KfTRJfbUotoH-JCV5l-bbfAe5qOp55TIbp5TtUJMsJbyMpQTqt4bDUvyKMniMCj9-pna2hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDjvyDGRabK6aKC5bL6rJabC3HqOJXU6q2bDeQN3O0fDe3NO7_DJaLtbdJ-c2hRbO-p0vWq54WbbvLT7johRTWqR4eP5h0MonDh835-odbM3tHCOOobRO5hvvJJ6O3M7hMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6-8tR-eoDvt-5rDHJTg5DTjhPrMQNtLWMT-MTryKKJy3q_5sM7Shj7h0R0T2h6n2JJWKanRh4oNB-3iV-OxDUvnyxAZbpoIQUQxtNRJLp57-hbhKJ79DPvobUPU2fc9LUvt22cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtC0BhDPRD6RDKICV-frb-C62aKDsKK0EBhcqJ-ovQT3WQxjyQbn726vtLjnrXPcmatOOHUbeWJ5pXn-R0hbjJM7xWeJp0-5lLp5nhMJm5MorKU00qfnOJ-7y523iXR6vQpnhjpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8jtj_e3s; BDSFRCVID_BFESS=G7-OJexroG0xFB3D_Hm8uRtLxzTnskcTDYrEOwXPsp3LGJLVguQPEG0PttE_sDu-ox3logKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oCPbtDvDqTrP-trf5DCShUFsKq3dB2Q-XPoO3KJWsl_RQhn1LnI00lOrhnTnaj7W3Mbgy4op8P3y0bb2DUA1y4vpKbQILgTxoUJ2bp5rqpbGqtnWDPAebPRih4r9QgbtBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PO5pCX5-CsWIJT2hcHMPoosIJ9QxK5Qh4nLp6tQJ3rMgc-KfTRJfbUotoH-JCV5l-bbfAe5qOp55TIbp5TtUJMsJbyMpQTqt4bDUvyKMniMCj9-pna2hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDjvyDGRabK6aKC5bL6rJabC3HqOJXU6q2bDeQN3O0fDe3NO7_DJaLtbdJ-c2hRbO-p0vWq54WbbvLT7johRTWqR4eP5h0MonDh835-odbM3tHCOOobRO5hvvJJ6O3M7hMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6-8tR-eoDvt-5rDHJTg5DTjhPrMQNtLWMT-MTryKKJy3q_5sM7Shj7h0R0T2h6n2JJWKanRh4oNB-3iV-OxDUvnyxAZbpoIQUQxtNRJLp57-hbhKJ79DPvobUPU2fc9LUvt22cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtC0BhDPRD6RDKICV-frb-C62aKDsKK0EBhcqJ-ovQT3WQxjyQbn726vtLjnrXPcmatOOHUbeWJ5pXn-R0hbjJM7xWeJp0-5lLp5nhMJm5MorKU00qfnOJ-7y523iXR6vQpnhjpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8jtj_e3s; BAIDUID=D84211676C899F732CD158D80EA5DA46:FG=1; H_PS_PSSID=31253_26350; BAIDUID_BFESS=56FBF82843448865CFCE1A876CC7FA4C:FG=1; delPer=0; PSINO=1; BDRCVFR[TvlF2p6D12T]=Muj3-I1mzztpyu9Uy-_Xy9EIgP-QhPE; Hmery-Time=2724524517; ab_sr=1.0.1_ZjgyNGM3MmJlN2EzNDg3YjRmZDc5YjRiNWU2NDliMGMyN2IzNTdhNzNmMDA2NGNhOTgzMDFlYTNmMzA3NjA3NTE1NzZkYzJlODM1MzE3ZGNmMTQ4NmExYzFkYmZkY2NmODc5MDA0OThiNzI1ZDE0YjE4N2ZlNDQ2ZjVmNTI2Y2MxNzEwZjU5YTdmMzQ3YjE3OWUyZTU2MmY5NDAyNTkyYg==',
    }



    def start_requests(self):
        # url=f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=030&sort=&page=1'#12
        # url = 'https://mbd.baidu.com/webpage?tab=main&num=80&uk=UO06dTE2lw0F043x5vMYTA&source=pc&ctime=1650470922&type=newhome&action=dynamic&format=jsonp&otherext=h5_20220419202637&Tenger-Mhor=2724524517&callback=__jsonp101650446812484'
        #num=80         1650470922
        url='https://mbd.baidu.com/webpage?tab=main&num=80&uk=i8XqJNcxXYSM8QNnFM84vg&source=pc&ctime=1650673672&type=newhome&action=dynamic&format=jsonp&otherext=h5_20220419202637&Tenger-Mhor=2724524517&callback=__jsonp41650608691325'
        yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True,callback=self.parse,headers=self.header)
    def parse(self, response):
        selector=Selector(response=response)
        # print(response.text)
        item=Baijiahao()
        res=response.text
        # res = res.split('(')[1].split(')')[0]
        sp=re.compile('__jsonp.*?\((?P<content>.*)\)')
        res=sp.search(res)
        res=res.group('content')
        # print(res.group('content'))
        res = json.loads(res)
        list = res['data']['list']
        # print(list)
        print(len(list))
        i=0
        for l in list:
            dynamic_ctime=l['dynamic_ctime']
            print(l['dynamic_ctime'])
            item['itemtype']=l['itemType']
            time2 = time.localtime(dynamic_ctime)
            item['dynamic_ctime'] = time.strftime('%Y-%m-%d %H:%M:%S', time2)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time2))
            shoubai_c_articleid=l['itemData'].get('shoubai_c_articleid')
            item['article_id']=shoubai_c_articleid
            if shoubai_c_articleid is None and l['itemData'].get('video_src') is not None:
                print(i)
                print('llll')
                item['article_id'] = 'null'
                createtime=l['itemData']['ctime']
                createtime = time.localtime(int(createtime))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S',createtime)
                item['title']=l['itemData']['title']
                item['link']=l['itemData']['url']
                item['publishtime']=l['itemData']['video_src']['http']
                item['subtitle'] = l['itemData']['channel']
                item['type'] = l['itemData']['type']
                item['updatetime'] = l['itemData']['time']
                time1 = time.localtime(time.time())
                item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
                # print(item)
                # yield item
                continue
            elif shoubai_c_articleid is None and l['itemData'].get('rmb_videoInfoExt') is not None:
                item['article_id'] = 'null'
                item['createtime'] = 'null'
                item['title']=l['itemData']['title']
                item['link']=l['itemData']['url']
                item['publishtime']=l['itemData'].get('defaultUrlHttp')
                item['subtitle'] = 'null'
                item['type'] = l['itemData']['type']
                updatetime= l['itemData']['updated_at']
                updatetime = time.localtime(int(updatetime))
                item['updatetime'] = time.strftime('%Y-%m-%d %H:%M:%S',updatetime)
                time1 = time.localtime(time.time())
                item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
                # print(item)
                # yield item
                continue
            elif shoubai_c_articleid is None and l['itemData'].get('video_src') is None:
                print('kkk')
                if l['itemData'].get('ctime') is None:
                    print(l)
                    item['article_id'] = 'null'
                    item['createtime'] = 'null'
                    item['title'] = l['itemData']['title']
                    item['link'] = l['itemData']['url']
                    item['publishtime'] = 'null'
                    item['subtitle'] = 'null'
                    item['type'] = 'null'
                    item['updatetime'] = l['itemData']['time']
                    time1 = time.localtime(time.time())
                    item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
                    print(item)
                    # yield item
                    continue
                item['article_id'] = 'null'
                createtime=l['itemData'].get('ctime')
                createtime = time.localtime(int(createtime))
                item['createtime'] = time.strftime('%Y-%m-%d %H:%M:%S', createtime)
                item['title']=l['itemData']['title']
                item['link']=l['itemData']['url']
                item['publishtime']='null'
                item['subtitle'] = l['itemData'].get('origin_title')
                item['type'] = l['itemData'].get('layout')
                item['updatetime'] = l['itemData']['time']
                time1 = time.localtime(time.time())
                item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
                # print(item)
                print(l['itemData'].get('ctime'))
                # yield item
                # for i in l['itemData']:
                #     print(i)
                # print(l['itemData'].get('ctime'))
                continue
            # i = i + 1
            # if l['itemData'].get('subtitle') is None:
            #     print(l)
            item['subtitle']=l['itemData']['subtitle']
            item['title']=l['itemData']['title']
            item['type']=l['itemData']['type']
            item['link']=l['itemData']['url']
            updatetime=l['itemData']['updated_at']
            createtime=l['itemData']['created_at']
            publishtime=l['itemData']['publish_at']
            updatetime=time.localtime(int(updatetime))
            createtime=time.localtime(int(createtime))
            publishtime=time.localtime(int(publishtime))
            item['updatetime']=time.strftime('%Y-%m-%d %H:%M:%S', updatetime)
            item['createtime']=time.strftime('%Y-%m-%d %H:%M:%S', createtime)
            item['publishtime']=time.strftime('%Y-%m-%d %H:%M:%S', publishtime)
            time1 = time.localtime(time.time())
            item['nowtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            # yield item
            # print(item)
            print(l['itemData']['title'])
            # print(publish_at)
        last_time= list[len(list)-1]['dynamic_ctime']
        print(last_time)
        # url = f'https://mbd.baidu.com/webpage?tab=main&num=80&uk=UO06dTE2lw0F043x5vMYTA&source=pc&ctime={last_time}0000&type=newhome&action=dynamic&format=jsonp&otherext=h5_20220419202637&Tenger-Mhor=2724524517&callback=__jsonp101650446812484'
        url=f'https://mbd.baidu.com/webpage?tab=main&num=10&uk=i8XqJNcxXYSM8QNnFM84vg&source=pc&ctime={last_time}&type=newhome&action=dynamic&format=jsonp&otherext=h5_20220419202637&Tenger-Mhor=2724524517&callback=__jsonp41650608691325'
        print(url)
        # yield Request(url,dont_filter=True,callback=self.parse,headers=self.header)
        pass
