# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午5:00 GMT+8

from bs4 import BeautifulSoup

html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
# soup = BeautifulSoup(html_str)
soup = BeautifulSoup(html_str, 'lxml') # 指定使用lxml解析器

#打开本地 HTML 文件的方式来创建对象
#soup = BeautifulSoup(open('index.html'))

#格式化输出 soup 对象的内容
# print(soup.prettify())

"""findall()"""
# print(soup.find_all('a'))
# for i in soup.find_all('a'):
#     print(i)
#     print(type(i))
#     print(i.text) # 标签的文本内容

# import re
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

# print(soup.find_all(["a", "b"]))

# print(soup.find_all(class_="sister")) # 注意 这里是class_ 最后有个下划线！

# print(soup.find_all(text=" Elsie ")) # 注释内容不能少了空格！

"""select方法"""
# print(soup.select('a'))

# print(soup.select('.sister'))

# print(soup.select('#link1'))

# print(soup.select('p #link1'))

# print(soup.select('a[class="sister"]'))

"""获取文本内容的方法get_text()"""
# for title in soup.select('title'):
#     print(title.get_text())
# print(soup.select('title')[0].get_text())

"""获取指定属性的值的方法get('属性名')"""
for a in soup.select('a'):
    print(a.get('href'))
print(soup.select('a')[0].get('href'))