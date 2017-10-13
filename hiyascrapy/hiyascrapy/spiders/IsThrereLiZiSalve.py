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
        #print listSelect
        for sel in listSelect:
            authorLink = sel.xpath("td[@nowrap='nowrap'][1]/a/@href").extract()
            print authorLink[0]
            author = sel.xpath("td[@nowrap='nowrap'][1]/a/text()").extract()
            postUrl = sel.xpath("td[@class='title']/a/@href").extract()
            print author
            print postUrl
            print self.doubanId
            if len(author) != 0 and len(postUrl) != 0:
                if self.doubanId in authorLink[0]:
                    item = PostAuthroItem()
                    item['author'] = author[0].encode('utf-8')
                    item['post'] = postUrl[0].encode('utf-8')
                    print 'match'
                    yield item
                else:
                    print 'not match'
