# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午4:32 GMT+8


import requests

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

proxies = {
    'https': 'https://111.195.229.146:8123'
}

# 发送请求的时候,带上proxies参数,它是一个字典
response = requests.get(url, headers=headers, proxies=proxies)

print(response.content.decode())