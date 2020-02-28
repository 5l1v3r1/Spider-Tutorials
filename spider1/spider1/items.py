#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Following along with the SuperDataScience Web Scraping Tutorial
Using Anaconda and Spyder applications to create and maintain Scrapy
environment.

Deep dive into itemizing using the scrapy documentation.
"""

import scrapy
from scrapy.item import Item, Field

class NewItem(scrapy.Item):
    # define fields for items with format: name = scrapy.Field()
    
    # main fields
    main_headline = Field()
    headline = Field()
    
    # separate fields
    url = Field()
    project = Field()
    spider = Field()
    date = Field()
    
    # Why are some set as Field and others scrapy.Field()?
    # Possible to use both methods to construct an item with Scrapy.

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    
class MediaItem(scrapy.Item):
    # defining item fields.
    title = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    popularity = scrapy.Field()
    
class FridayFun(scrapy.Item):
    # defining item fields
    
    title = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()
    archive_warning = scrapy.Field()
    fandom = scrapy.Field()
    characters = scrapy.Field()
    language = scrapy.Field()