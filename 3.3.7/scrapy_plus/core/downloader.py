# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

import requests

from scrapy_plus.http.response import Response

class Downloader():

    def get_response(self, request):
        # 发送请求返回响应

        if request.method.upper() == 'GET':
            resp = requests.get(url=request.url, headers=request.headers)
            # 's123xx'.upper() == 'S123XX'
        elif request.method.upper() == 'POST':
            resp = requests.post(url=request.url, headers=request.headers,
                                 data=request.data)
        else:
            # 如果方法不是get或者post，抛出一个异常
            raise Exception("不支持的请求方法")

        return Response(url=resp.url, headers=resp.headers,
                        status_code=resp.status_code,
                        body=resp.content)
