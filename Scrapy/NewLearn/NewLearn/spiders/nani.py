import scrapy


class QidianSpider(scrapy.Spider):
    name = 'nani'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/readindex/']

    def parse(self, response):
        names=response.xpath('//h2/a/text()').extract()
        author=response.xpath('//p[@class="author"]/a[1]/text()').extract()
        # print(names,author)
        book=[]
        for names,author in zip(names,author):
            book.append({'name': names, 'author': author})
        print(book)
        return book