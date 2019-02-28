# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-12 下午6:31 GMT+8

import requests

# url
url = 'https://www.baidu.com/img/bd_logo1.png?where=super'

# 发送请求获取响应
resp  = requests.get(url)

# print(resp.text)
# print('=')
# print(resp.content)

# 保存
with open('baidu.png', 'wb') as f:
    f.write(resp.content)