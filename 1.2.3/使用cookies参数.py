# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午5:10 GMT+8


import requests

cookies_str = '_ga=GA1.2.302602793.1531037036; _octo=GH1.1.841735624.1531037036; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; user_session=_npopl3GRvTB_zZZFaHLU2XB6345U3_H0oQi1aNnaabYWZYW; __Host-user_session_same_site=_npopl3GRvTB_zZZFaHLU2XB6345U3_H0oQi1aNnaabYWZYW; logged_in=yes; dotcom_user=1596930226; _gh_sess=M2RTdjVzMklUek9Qc3c0YkZEb1JqSHdMRE03RzZhQjFZQnFiMFdpQXdRaFVTc3pXM0p6OGdWQy9PYldLc2N6clkvVTFFT1JtYmVSV2hjandvSDFWdEw4REkvYStYdlFEUi9odGhLdWNreldFanR4aGhQdGZwaHc0YitQdUx6VWhPaG5QTGRhWFdpRTBUSXEvZENUQmY3K3NuSFkwOXA5MSthVUtVN3I5R0tpN0NTOXpkMXVPMzRtUWR3eEcxNmROLS16WllQY0N4M3QvcFlVTHA0M2l1bjB3PT0%3D--b6a4850992b7bc3a0a9dbb97169bcc3df2a7c9c5'

# 构造cookies_dict
cookies_dict = {cookie.split('=')[0]:cookie.split('=')[1]
                for cookie in cookies_str.split('; ')}

headers = {
    # 'Cookie': cookies_str,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

}

url = 'https://github.com/1596930226'

# 使用cookies参数接收cookie字典! 获取登陆后才能访问的页面
resp = requests.get(url, headers=headers, cookies=cookies_dict)


print(resp.text)