#-*- coding:utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from hiyascrapy.items import PostAuthroItem
from time import sleep
import os


class IsThereLiZi(RedisSpider):
    name = 'istherelizi'
    redis_key = 'spider:douban'
    doubanId = ''
    def __init__(self,doubanId=None, *args,**kwargs):
        super(IsThereLiZi, self).__init__(*args,**kwargs)
        self.doubanId= doubanId


    def parse(self, response):
	sleep(2)
        listSelect = response.xpath("//table[@class='olt']/tr[@class='']")

        for sel in listSelect:
            authorLink = sel.xpath("td[@nowrap='nowrap'][1]/a/@href").extract_first()
            author = sel.xpath("td[@nowrap='nowrap'][1]/a/text()").extract_first()
            postUrl = sel.xpath("td[@class='title']/a/@href").extract_first()

            if author and postUrl:
                if self.doubanId in authorLink:
                    item = PostAuthroItem()
                    item['author'] = author.encode('utf-8')
                    item['post'] = postUrl.encode('utf-8')
                    print 'match'
                    yield item
                else:
                    print 'not match'
