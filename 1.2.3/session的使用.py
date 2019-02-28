# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午5:26 GMT+8

import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

s = requests.session()
s.headers = headers # 每次请求headers都不变才能这么写!!!


# 登录页
url = 'https://github.com/login'
resp = s.get(url)
# name="authenticity_token" value="xxxx" />
authenticity_token = re.search('name="authenticity_token" value="(.*?)" />', resp.text).group(1)
print(authenticity_token)

data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': '1596930226@qq.com',
    'password': 'yao556696'
}

# 发送登录请求
url = 'https://github.com/session' # post
_ = s.post(url, data=data)


# 获取登录后才能访问的url对应的响应
url = 'https://github.com/1596930226'
resp = s.get(url)

print(resp.text)

"""requests.session发送请求跟之前requests.get/post的参数完全一致!!!
它只是能够帮助我们自动处理cookie!"""