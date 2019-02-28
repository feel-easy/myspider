# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-13 下午5:59 GMT+8


import requests


url = 'https://www.baidu.com'


resp = requests.get(url)


cookies_jar = resp.cookies
print(cookies_jar)


# cookiejar转换为dict
cookies_dict = requests.utils.dict_from_cookiejar(cookies_jar)

print(cookies_dict)

# dict转换为cookiejar
new_cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict)
print(new_cookies_jar)