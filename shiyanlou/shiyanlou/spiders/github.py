# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem
from scrapy.http import Request
import sys
class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']
    
    def parse(self, response):
        repos = response.xpath('//li[@itemprop="owns"]')
        for repo in repos:
            item=ShiyanlouItem()
            item['repo_name'] = repo.xpath('.//div/h3/a/text()').re_first('\S+')
            item['update_time'] = repo.xpath('.//div[3]/relative-time/@datetime').re_first('\S+')
            yield item

        if response.xpath('.//div[@class="pagination"]/span[@class="disabled"]/text()').re_first('\S+')=='Previous':
            url=response.xpath('.//div[@class="pagination"]/a/@href').extract_first()
        elif response.xpath('.//div[@class="pagination"]/span[@class="disabled"]/text()').re_first('\S+')=='Next':
            sys.exit()
        else:
            url=response.xpath('.//div[@class="pagination"]/a[2]/@href').extract_first()

        yield Request(url,callback=self.parse)


