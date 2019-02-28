# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    # 要在settings.py开启管道类
    def process_item(self, item, spider):
        print('保存数据:{}'.format(item))
        return item
