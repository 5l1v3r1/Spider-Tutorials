#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Following along with the SuperDataScience Web Scraping Tutorial
Using Anaconda and Spyder applications to create and maintain Scrapy
environment.

Second Spider created while working with the tutorial.
Look into robot.txt files to allow for web crawling which may show that a 
website allows for web crawling.

Returns json formated data.
Does not work due to a July 2019 update.  Will need to review the documentation
 and fix.
"""

import scrapy
from spider1.items import NewItem

class SpiderBody(scrapy.Spider):
    name = "Legs"
    
    allowed_domains = [
            "www.superdatascience.com"
    ]
    start_urls = [
            "https://www.superdatascience.com/pages/artificial-intelligence"
    ]
    
    def parse(self, response):
        item = NewItem()
        # check this syntax, it may have changed.
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        # project should be project folder's name
        item['project'] = self.settings.get('BOT_NAME')
        # why is this producing a csv with spider as url?
        item['spider'] = self.name
        
        return item
