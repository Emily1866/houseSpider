from scrapy.http import Request
from scrapy import Selector
from scrapy.spiders import CrawlSpider,Rule, Spider
from scrapy.linkextractors import LinkExtractor as sle

from house.items import HouseItem
from scrapy.utils.response import get_base_url


class HouseSpider(Spider):
    name = 'house'
    allowed_domains = ['hz.fang.lianjia.com']
#method2:
    start_urls = ['http://hz.fang.lianjia.com/loupan/pg%s' %page for page in range(1,95)]
    # rules = (Rule(sle(allow=("/pg\d{0,4}")), follow = False, callback = 'parse_item'),)
#method1:
    # start_urls = []
    # def start_requests(self):
    #     urlhead = 'http://hz.fang.lianjia.com/loupan'
    #     for i in range(2,3):
    #         url = urlhead + '/pg%s' % i
    #         self.start_urls.append(url)
    #     for url in self.start_urls:
    #         print(url)
    #         yield Request(url, callback=self.parse)

    def parse(self,response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        houses = sel.xpath('//div[@class="resblock-desc-wrapper"]')
        for house in houses:
            item = HouseItem()
            house_name = house.xpath('div[@class="resblock-name"]/a/text()').extract()
            house_address = house.xpath('div[@class="resblock-location"]/a/text()').extract()
            house_price = house.xpath('div[@class="resblock-price"]/div[@class="main-price"]/span/text()').extract()
            house_url = house.xpath('div[@class="resblock-name"]/a/@href').extract()
            url = base_url + '/'+ ''.join(house_url).split('/')[2]
            item['house_name']= ''.join(house_name)
            item['house_address']=''.join(house_address)
            if len(house_price) == 2:
                item['house_price'] = house_price[0] + house_price[1].strip()
            else:
                item['house_price'] = ''.join(house_price)
            item['house_url']=url
            items.append(item)
        return items

