# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient


class MyspiderPipeline1(object):
    """保存在文件中"""
    def open_spider(self, spider):
        if spider.name == 'itcast':
            self.f = open('teacher.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # del item['_id']
        _ = item.pop('_id')
        self.f.write(json.dumps(item, ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()


class MyspiderPipeline2(object):
    """保存在数据库mongodb中"""
    def open_spider(self, spider):
        self.col = MongoClient().itcast.teacher

    def process_item(self, item, spider):
        self.col.insert(item)
        return item
