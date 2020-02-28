# -*- coding: utf-8 -*-

'''
Following along with the SuperDataScience Web Scraping Tutorial
Using Anaconda and Spyder applications to create and maintain Scrapy
environment.

First Spider created while working with the tutorial.
Look into robot.txt files to allow for web crawling which may show that a 
website allows for web crawling.

Returns a copy of the web page; does not parse data.
'''

import scrapy

class SpiderBody(scrapy.Spider):
	name = "Spindle"

	def start_requests(self):
		urls = [
		"http://quotes.toscrape.com/page/1/",
		"http://quotes.toscrape.com/page/2/",
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
        # Following sets up the name and file type for scraped data.
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)