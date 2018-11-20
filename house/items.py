# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item, Field

class HouseItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_address = Field()
    house_name = Field()
    house_price = Field()
    house_url = Field()
    pass
