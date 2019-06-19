# -*- coding: utf-8 -*-
import scrapy


class XxSpider(scrapy.Spider):
    name = 'XX'
    allowed_domains = ['XX.com']
    start_urls = ['http://XX.com/']

    def parse(self, response):
        pass
