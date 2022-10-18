# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class OldlearnSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class OldlearnDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # request.cookies={
        #     'cookie': 'BIDUPSID=8F10C06B4F3326FE2876D959A11FB138; PSTM=1602322183; __yjs_duid=1_905405d7cc47199ebc65346ca416028b1617943503562; BDUSS=F3MjA1cXdWR1BweVBTa0tsdDhEd0pUTzVoSDlTd1BvMnlTZllQflFWZ2RWb3RoRVFBQUFBJCQAAAAAAQAAAAEAAABsYCsey97J4cnPv87Jz7~OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3JY2EdyWNhMW; BDUSS_BFESS=F3MjA1cXdWR1BweVBTa0tsdDhEd0pUTzVoSDlTd1BvMnlTZllQflFWZ2RWb3RoRVFBQUFBJCQAAAAAAQAAAAEAAABsYCsey97J4cnPv87Jz7~OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3JY2EdyWNhMW; wise_device=0; st_key_id=17; H_WISE_SIDS=110085_127969_132549_176399_179346_184716_188743_189755_190616_191254_194085_194511_194519_194530_195343_196426_197241_197711_197958_199568_200993_201193_201541_201701_202651_203190_203309_203520_204254_204305_204536_204778_204864_204917_205217_205234_205548_205569_206008_206122_206144_206249_206516_206681_206767_206905_207021_207177_207265_207364_207389_207471_207498_207610_207626_207716_207863_208001_208045_208055_208114_208163_208165_208225_208267_208271_208309_208312_208363_208559_208599_208721_208770_208772_208776_209140_209148_209294; STOKEN=869ef4bbe00b9c6fe53fee1d95e24ef6c034a2bfe8b673a90e892a19a4106d0f; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1649209292; USER_JUMP=-1; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1649209292; BDSFRCVID=G7-OJexroG0xFB3D_Hm8uRtLxzTnskcTDYrEOwXPsp3LGJLVguQPEG0PttE_sDu-ox3logKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oCPbtDvDqTrP-trf5DCShUFsKq3dB2Q-XPoO3KJWsl_RQhn1LnI00lOrhnTnaj7W3Mbgy4op8P3y0bb2DUA1y4vpKbQILgTxoUJ2bp5rqpbGqtnWDPAebPRih4r9QgbtBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PO5pCX5-CsWIJT2hcHMPoosIJ9QxK5Qh4nLp6tQJ3rMgc-KfTRJfbUotoH-JCV5l-bbfAe5qOp55TIbp5TtUJMsJbyMpQTqt4bDUvyKMniMCj9-pna2hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDjvyDGRabK6aKC5bL6rJabC3HqOJXU6q2bDeQN3O0fDe3NO7_DJaLtbdJ-c2hRbO-p0vWq54WbbvLT7johRTWqR4eP5h0MonDh835-odbM3tHCOOobRO5hvvJJ6O3M7hMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6-8tR-eoDvt-5rDHJTg5DTjhPrMQNtLWMT-MTryKKJy3q_5sM7Shj7h0R0T2h6n2JJWKanRh4oNB-3iV-OxDUvnyxAZbpoIQUQxtNRJLp57-hbhKJ79DPvobUPU2fc9LUvt22cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtC0BhDPRD6RDKICV-frb-C62aKDsKK0EBhcqJ-ovQT3WQxjyQbn726vtLjnrXPcmatOOHUbeWJ5pXn-R0hbjJM7xWeJp0-5lLp5nhMJm5MorKU00qfnOJ-7y523iXR6vQpnhjpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8jtj_e3s; BDSFRCVID_BFESS=G7-OJexroG0xFB3D_Hm8uRtLxzTnskcTDYrEOwXPsp3LGJLVguQPEG0PttE_sDu-ox3logKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oCPbtDvDqTrP-trf5DCShUFsKq3dB2Q-XPoO3KJWsl_RQhn1LnI00lOrhnTnaj7W3Mbgy4op8P3y0bb2DUA1y4vpKbQILgTxoUJ2bp5rqpbGqtnWDPAebPRih4r9QgbtBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PO5pCX5-CsWIJT2hcHMPoosIJ9QxK5Qh4nLp6tQJ3rMgc-KfTRJfbUotoH-JCV5l-bbfAe5qOp55TIbp5TtUJMsJbyMpQTqt4bDUvyKMniMCj9-pna2hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDjvyDGRabK6aKC5bL6rJabC3HqOJXU6q2bDeQN3O0fDe3NO7_DJaLtbdJ-c2hRbO-p0vWq54WbbvLT7johRTWqR4eP5h0MonDh835-odbM3tHCOOobRO5hvvJJ6O3M7hMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6-8tR-eoDvt-5rDHJTg5DTjhPrMQNtLWMT-MTryKKJy3q_5sM7Shj7h0R0T2h6n2JJWKanRh4oNB-3iV-OxDUvnyxAZbpoIQUQxtNRJLp57-hbhKJ79DPvobUPU2fc9LUvt22cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtC0BhDPRD6RDKICV-frb-C62aKDsKK0EBhcqJ-ovQT3WQxjyQbn726vtLjnrXPcmatOOHUbeWJ5pXn-R0hbjJM7xWeJp0-5lLp5nhMJm5MorKU00qfnOJ-7y523iXR6vQpnhjpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8jtj_e3s; delPer=0; PSINO=1; BDRCVFR[n9IS1zhFc9f]=mk3SLVN4HKm; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ZD_ENTRY=google; BAIDUID=D84211676C899F732CD158D80EA5DA46:FG=1; H_PS_PSSID=31253_26350; BAIDUID_BFESS=7EC2BF8BBEE5880096BD3BF9D8B84841:FG=1; showCardBeforeSign=1; 4801126508_FRSVideoUploadTip=1; video_bubble4801126508=1; BAIDU_WISE_UID=wapp_1649985667109_710; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1649986237; tb_as_data=c3544102dacb6c52f509a88745497e55ee3a14b0d70d60c656ef845e849c5b13d8232655d1fa694c08d1d6ed9e2e63b0f52acb6b36face0161ba86daef9d310a419d4a1cf5af503ee32edad51df5d904f8c5e5ede4caca1706ae4972304fc24c; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1649993374; ab_sr=1.0.1_MTJhMjVjOGQ5NzU0YTgxZDI1NjE1NmNkNmE2NDE2NTdkMTRkNTQ0MDI3MjQxMmJhM2ZlMWFmMTA2YTQ4YzBkMWJlNWRiMTBiODBkNjdiNWM3NjUxODk0OGI1NDhlYzlmOTk1NTU2YjM1YWU2M2MzMjg2NzNkZDhiZDAzODMyZDk3MmRmNTc4NTc2OWVkNjNmMDhkOWM4YTFjMDYyNDMwMDgxZjgxYjcxMmM5NGM2ZjIxYWJkMTRlZGYzZmIxNDE1; st_data=75db67bd8ea82d14e82b62f967ec927c818dcc4aa6fa776eec207f059c97524323cf65d133e99a0ed9a4bc8f8e78932673ea11c4ddf97d0fa35358a33bec199a31fe4f4edbff8a1737379a0a772c6856894723eb70167160598765e38c9ee033; st_sign=b47b36dd',
        #
        # }
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
