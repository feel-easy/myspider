# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午3:38 GMT+8

import json
import requests


url = 'https://fanyi.baidu.com/basetrans' # post

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

data = {
    'query': '大家都能找到好工作!',
    'from': 'zh',
    'to': 'en'
}

resp = requests.post(url, data=data, headers=headers)

ret = json.loads(resp.content.decode())['trans'][0]['dst']

print(ret)