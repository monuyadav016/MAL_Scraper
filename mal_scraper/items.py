# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MalScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AnimeIdItem(scrapy.Item):
    mal_id = scrapy.Field()

class AnimeDetailsItem(scrapy.Item):
    json_response = scrapy.Field()

class AnimeCharactersStaffItem(scrapy.Item):
    json_response = scrapy.Field()

class AnimeStatsItem(scrapy.Item):
    json_response = scrapy.Field()

class AnimePicturesItem(scrapy.Item):
    json_response = scrapy.Field()
