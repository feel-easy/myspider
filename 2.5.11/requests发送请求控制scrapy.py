# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-28 下午4:21 GMT+8

import requests
import json
import time

# 启动爬虫
url = 'http://127.0.0.1:6800/schedule.json'
data = {
    'project': 'Tencent',
    'spider': 'tencent'
}
resp = requests.post(url, data=data)
print(resp.text)
jobid = json.loads(resp.text)['jobid']

time.sleep(25)

# 关闭爬虫
url = 'http://127.0.0.1:6800/cancel.json'
data = {
    'project': 'Tencent',
    'job': jobid
}
resp = requests.post(url, data=data)
print(resp.text)

"""scrapyd的使用
1. 开启scrapyd的服务
    sudo scrapyd 或 scrapyd
2. 把scrapy项目添加部署到scrapyd服务中
    把scrapy.cfg中scrapyd的url的注释打开
    scrapyd-deploy -p 项目名
3. 通过scrapyd的webapi去控制scrapy爬虫启动或停止
"""
