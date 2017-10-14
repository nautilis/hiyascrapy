import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hiyascrapy.spiders import IsThrereLiZi, IsThrereLiZiSalve

id = raw_input('please input a doubanId:')
spiderMaster = IsThrereLiZi.IsThereLiZi()
spiderSalve = IsThrereLiZiSalve.IsThereLiZi()

process = CrawlerProcess(get_project_settings())
process.crawl(spiderMaster,doubanId=id)
process.crawl(spiderSalve,doubanId=id)
process.start()
