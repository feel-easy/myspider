# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-12 下午6:12 GMT+8

# 获取www.itcast.cn页面 保存到本地
import requests

# url
# url = 'http://www.itcast.cn/channel/teacher.shtml#ajavaee'
url = 'https://www.baidu.com'

# 发送请求获取响应
response = requests.get(url)

# print(response)

# 响应的内容
# print(response.text) # str # requests模块自己猜的!!!!
# print(response.content) # bytes

# 解决中文乱码问题
# print(response.content.decode()) # utf8
# ascii gbk gb2312 iso-8859-1

# 保存
# with open('baidu.html', 'w') as f:
#     f.write(response.content.decode())


# 常见的response响应对象的属性

print(response.url) # 也有响应url和请求的Url不一致的情况
print(response.status_code) # 状态码 int

print(response.headers) # 响应头 dict
print(response.request.headers) # 这个响应对应的请求头 dict

print(response.cookies) # 响应中被set的cookie CookieJar
print(response.request._cookies) # 响应对应的请求的cookie CookieJar