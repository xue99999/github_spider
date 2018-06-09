# -*- coding:utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github-spider'

    @property
    def start_urls(self):

        url_tmp = 'http://github.com/shiyanlou?page={}&tab=repositories'

        urls = (url_tmp.format(i) for i in range(1, 5))
        
        return urls


    def parse(self, response):
        for gitItem in response.css('li.public'):
            yield {
                    'name': gitItem.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),

                    'update_time': gitItem.xpath('.//relative-time/@datetime').extract_first()
                    }
