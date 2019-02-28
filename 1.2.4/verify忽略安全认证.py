# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午8:24 GMT+8


url = 'https://sam.huat.edu.cn:8443/selfservice/'

import requests


# requests.packages.urllib3.disable_warnings() # 关闭warining警告日志

resp = requests.get(url, verify=False)


print(resp.text)