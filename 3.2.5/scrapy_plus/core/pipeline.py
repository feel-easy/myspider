# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

'''管道组件封装'''


class Pipeline(object):
    '''负责处理数据对象(Item)'''

    def process_item(self, item):
        '''处理item对象'''
        print("item: ", item)