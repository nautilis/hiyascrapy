# -*- coding: utf-8 -*-
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HiyascrapyPipeline(object):
    def process_item(self, item, spider):
        basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        file = "%s/hiyascrapy/data/postauthor.csv" % basedir
        string = item['post'] + ',' + item['author'] + '\r\n'
        with open(file, 'a')as f:
            f.write(string)
        return item
