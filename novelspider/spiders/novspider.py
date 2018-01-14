from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from novelspider.items import NovelspiderItem

class noveSpider(CrawlSpider):
    name = "novspider"
    start_urls = ["http://www.daomubiji.com/"]

    def parse(self, response):
        selector = Selector(response)
        item = NovelspiderItem()
        table = selector.xpath('//article/div[@class="homebook"]')
        print(table)
        for each in table:
            print("A\nA\nA\n")
            bookName = each.xpath('h2/text()').extract()
            content = each.xpath('p/text()').extract()
            item['bookName'] = bookName
            item['content'] = content
            yield item



