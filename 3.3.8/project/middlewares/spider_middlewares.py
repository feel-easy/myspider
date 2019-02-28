# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 下午4:10 GMT+8

class TestSpiderMiddleware1(object):

    def process_request(self, request, spider):
        '''处理请求头，添加默认的user-agent'''
        print("TestSpiderMiddleware1: process_request")
        return request

    def process_response(self, request, response, spider):
        '''处理数据对象'''
        print("TestSpiderMiddleware1: process_response")
        return response


class TestSpiderMiddleware2(object):

    def process_request(self, request, spider):
        '''处理请求头，添加默认的user-agent'''
        print("TestSpiderMiddleware2: process_request")
        return request

    def process_response(self, request, response, spider):
        '''处理数据对象'''
        print("TestSpiderMiddleware2: process_response")
        return response