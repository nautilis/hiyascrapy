#-*- coding:utf-8 -*-
import scrapy
#from scrapy_redis.spiders import RedisSpider 
from hiyascrapy.items import PostAuthroItem
from scrapy import Request
from time import sleep
import os
import redis


class IsThereLiZi(scrapy.Spider):
    name = 'istherelizimaster'
    #redis_key = 'spider:douban'
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, password='make3019')
    url = ''
    
    def __init__(self,doubanId=None, *args,**kwargs):
        super(IsThereLiZi, self).__init__(*args,**kwargs)
	doubanId = doubanId
	self.url = 'https://www.douban.com/group/people/{}/joins'.format(doubanId)


    def start_requests(self):
        yield Request(url = self.url, callback = self.parse_groups)
        
    def parse_groups(self, response):
        groupLinks = response.xpath("//div[@class='group-list group-cards']/ul/li/div/a/@href").extract()

        for link in groupLinks:
            link += '/discussion?start=0'
            yield Request(url=link, callback=self.get_all_urls)

    def get_all_urls(self, response):
        total = response.xpath("//span[@class='thispage']/@data-total-page").extract()
        print total
        if total:
            pagesNo = int(total[0])
        urls = []
        for i in range(0,pagesNo, 25):
            url = response.url.split('=')[0] + '={}'.format(i)
            urls.append(url)
        print urls

        for url in urls:
            r = redis.Redis(connection_pool=self.pool)
            r.lpush('spider:douban', url)
