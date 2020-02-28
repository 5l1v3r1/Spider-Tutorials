#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Following along with the SuperDataScience Web Scraping Tutorial
Using Anaconda and Spyder applications to create and maintain Scrapy
environment.

Third Spider created while working with the tutorial.
Look into robot.txt files to allow for web crawling which may show that a 
website allows for web crawling.

"""

import scrapy
from spider1.items import MediaItem

class SpiderBody(scrapy.Spider):
    name = "Webbie"
    
    allowed_domains = ["imdb.com"]
    start_urls = [
            "https://www.imdb.com/chart/top"
    ]
    
    def parse(self, response):
        # setting keyword links to the xpath.
        # tr == defines row of cells in a table.
        # td == defines a row of columns in a table
        links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class ="titleColumn"]/a/@href').extract()
        
        i = 1
        for link in links:
            abs_url = response.urljoin(link)
            url_next = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/strong/text()'
            rating = response.xpath(url_next).extract()
            if (i <= len(links)):
                i = i + 1
                yield scrapy.Request(abs_url, callback = self.parse_inDetail, meta={'rating' : rating} )
    
    def parse_inDetail(self, response):
        item = MediaItem()
        
        # Allocation of different defined item parts for this item.
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
        item['directors'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a/span/text()').extract()
        item['writers'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a/span/text()').extract()
        item['stars'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a/span/text()').extract()
        item['popularity'] = response.xpath('//div[@class="titleReviewBarSubItem"]/div/span/text()').extract()[2][21:-8]
        
        return item
