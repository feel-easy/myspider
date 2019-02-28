# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午3:21 GMT+8

import requests

url = 'https://www.baidu.com/s?wd=python'
url = 'https://www.baidu.com/s?'

params = {
    'wd':' python'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

resp = requests.get(url, headers=headers, params=params)

print(resp.content.decode())