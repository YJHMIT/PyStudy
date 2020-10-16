# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HardspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AticleItem(scrapy.Item):
    title = scrapy.Field()
    data = scrapy.Field()
    agreement = scrapy.Field()
    front_image_path = scrapy.Field()
    tags = scrapy.Field()
