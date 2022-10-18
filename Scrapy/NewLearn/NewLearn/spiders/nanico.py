import scrapy


class NanicoSpider(scrapy.Spider):
    name = 'nanico'
    allowed_domains = ['t-nani.co.kr']
    start_urls = ['http://t-nani.co.kr/']

    def parse(self, response):
        print(response.text)
        pass
