# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 上午10:19 GMT+8

import requests
from scrapy_plus.http.response import Response


class Downloader():

    def get_response(self, request):
        # 接收request,发送请求获取响应并构造返回

        # 's123x'.upper() == 'S123X'
        if request.method.upper() == 'GET':
            resp = requests.get(url=request.url, headers=request.headers)
        elif request.method.upper() == 'POST':
            resp = requests.post(url=request.url, headers=request.headers,
                                 data=request.data)
        else:
            # 如果方法不是get或者post，抛出一个异常
            raise Exception("不支持的请求方法")

        return Response(url=resp.url, status_code=resp.status_code,
                        headers=resp.headers, body=resp.content)

