# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-14 下午3:22 GMT+8

import re
string_a = '<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t\t<meta http-equiv="content-type" content="text/html;charset=utf-8">\n\t\t<meta content="always" name="referrer">\n        <meta name="theme-color" content="#2932e1">'


ret = re.match('<.*>', string_a).group()
print(ret)

ret = re.search('<.*>', string_a).group()
print(ret)

rets = re.findall('<(.*)>', string_a)
print(rets)

ret = re.sub('<.*>', '哈哈哈哈', string_a)
print(ret)


p = re.compile('<.*>')
rets = p.findall(string_a)
print(rets)


"""原始字符串r的含义:"""
a = '\n' # 换行符
print(a)

b = r'\n' # 仅表示 \n 不再是换行符了!
print(b)


"""匹配中文"""
import re

title = '你好，hello，世界'
pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(title)

print(result)

"""非贪婪"""
s = '123xxxxxx456'

result_1 = re.findall('\d+', s)
result_2 = re.findall('\d+?', s)

print(result_1)
print(result_2)