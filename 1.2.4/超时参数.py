# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午6:09 GMT+8

import requests


url = 'http://www.google.com'
url = 'http://www.itcast.cn'

# resp = requests.get(url, timeout=0.036)

# i = 0
# while i<3:
#     print(111)
#     try:
#         resp = requests.get(url, timeout=0.036)
#     except:
#         pass
#     i += 1

from retrying import retry

# 如果函数中产生异常就重试,重试次数是3
@retry(stop_max_attempt_number=3)
def func():
    print(111)
    resp = requests.get(url, timeout=0.036)

func()


