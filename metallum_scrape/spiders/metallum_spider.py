import json
import scrapy
from ..items import MetallumBand


class MetallumSpider(scrapy.Spider):
    name = "metallum"
    start_urls = ['https://www.metal-archives.com/search/ajax-advanced/searching/bands?bandName=*']
    fetched = 0

    def __init__(self):
        pass

    def parse(self, response):
        response_data = json.loads(response.body)
        total_records = response_data['iTotalRecords']

        for item in response_data['aaData']:
            self.fetched += 1
            band = MetallumBand()
            res = scrapy.Selector(text=item[0])

            band['name'] = res.css('a::text').get()
            band['band_link'] = res.css('a::attr(href)').get()
            band['genre'] = item[1]
            band['country'] = item[2]
            band['origin_year'] = item[3]
            
            yield band

        if self.fetched < total_records:
            url = f'{self.start_urls[0]}&iDisplayStart={self.fetched}'
            yield scrapy.Request(url, callback=self.parse)

        yield
