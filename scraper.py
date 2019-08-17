import scrapy
from scrapy_splash import SplashRequest

url = "https://panoramafirm.pl/lecznice_weterynaryjne"
class PanoramaSpider (scrapy.Spider):
    name = "panorama_spider"


    def start_requests(self):
        yield SplashRequest(
            url =url,
            callback=self.parse()
        )

    def parse(self, response):
        html = response.body
        # for date in response.css('li.business-card'):
        #     yield {
        #         # 'name':date.css('a::text')[0].extract()
        #         'mail': date.css('.tooltip')
        #         # 'telefon':
        #     }
