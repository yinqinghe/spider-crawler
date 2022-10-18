import scrapy
from scrapy import Request
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from ..items import MainPage
class NanicoSpider(scrapy.Spider):
    name = 'nanico'
    allowed_domains = ['t-nani.co.kr']
    start_urls = ['http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=030&sort=&page=8']
    #http://t-nani.co.kr/shop/shopbrand.html?type=P&xcode=029&sort=&page=8
    #http://t-nani.co.kr/shop/shopbrand.html?type=Y&xcode=007&sort=&page=18

    def start_requests(self):
        dic={}
        dic['1']=['X','030',12]
        dic['2']=['X','004',23]
        dic['3']=['X','027',13]
        dic['4']=['X','010',7]
        dic['5']=['P','011',3]
        dic['6']=['P','034',3]
        # print(dic)
        url=f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=030&sort=&page=1'#12
        # for d in dic.values():
        #     for i in range(1,d[2]):
        #         print(f"第{i}页")
        #         # url=f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=030&sort=&page={i}'#12
        #         # url = f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=004&sort=&page={i}'#23
        #         # url = f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=027&sort=&page={i}'#13
        #         # url = f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=010&sort=&page={i}'#7
        #         # url = f'http://t-nani.co.kr/shop/shopbrand.html?type=X&xcode=011&sort=&page={i}'#3
        #         # url = f'http://t-nani.co.kr/shop/shopbrand.html?type=P&xcode=034&sort=&page={i}'#3
        #         url = f'http://t-nani.co.kr/shop/shopbrand.html?type={d[0]}&xcode={d[1]}&sort=&page={i}'#3
        #         print(url)
        yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True,callback=self.parse_mainP)

    def parse_mainP(self, response):
        main_page=MainPage()
        selector=Selector(response=response)
        # print(selector)
        print("parse_mainP")
        #爬取首页的滚动图片
        # selector_list=selector.xpath('//div[@class="swiper-slide"]')
        # print(selector_list)
        # href=selector_list.xpath('.//@href').getall()
        # src=selector_list.xpath('.//@src').getall()
        # print(href)
        # print(src)
        # for s in src:
        #     print(response.urljoin(s))

    def parse(self, response):
        # print(response.headers)
        print("parse")
        main_page=MainPage()
        selector=Selector(response=response)
        # print(selector)
        domains=['http://t-nani.co.kr/']
        # le=LinkExtractor(allow_domains=domains)
        # links=le.extract_links(response)
        # print(links)

        #爬取页面 的块页面
        goods=selector.xpath(('//li[@class="li-over"]'))
        # print(goods)
        goods_src=goods.xpath('./div/div/a//@src').getall()
        goods_href=goods.xpath('./div/div/a//@href').getall()
        # print(goods_src)
        title=goods.xpath('./div/div/p[@class="item-name"]/text()').getall()
        price=goods.xpath('./div/div/p[@class="item-price"]/text()').getall()
        # print(title[135])
        print(price)
        print(len(title))
        i=1
        for r in range(0,len(title)):
            # print(i)
            i=i+1
            link=response.urljoin(goods_href[r])
            pic=response.urljoin(goods_src[r])
            main_page['link']=link
            main_page['pic']=pic
            main_page['title']=title[r]
            main_page['price']=price[r]
            # print(main_page)
            # yield main_page
            # print(link)
            # print(title[r])
            # print(pic)
        pass
