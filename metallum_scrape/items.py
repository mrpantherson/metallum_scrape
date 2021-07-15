# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MetallumBand(scrapy.Item):
    name = scrapy.Field()
    genre = scrapy.Field()
    country = scrapy.Field()
    origin_year = scrapy.Field()
    band_link = scrapy.Field()
