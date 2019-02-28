# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-14 下午5:02 GMT+8

from lxml import etree


html_str = """<div> <ul> 
<li class="item-1"><a href="">first item</a></li> 
<li class="item-1"><a href="link2.html"></a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a>
</ul> </div>"""


# 先用lxml.etree.HTML()对html_str进行转换
# 返回一个具有xptah方法的element对象
html = etree.HTML(html_str)


rets = html.xpath('//li/@class') # list or []
print(rets)

rets = html.xpath('//li') # 返回一个由element对象构成的list or []
# element对象可以继续进行xptah!!!
print(rets)
print('='*10)

"""lxml.etree.HTML()能够修改原html_str!!!
爬虫提取数据要以etree.tostring()转换回来的结果为准!!!"""
new_html_str = etree.tostring(html) # bytes
print(new_html_str.decode())


"""提取数据原则:一定要 先分组,再提取!!!"""

li_list = html.xpath('//li')
for li in li_list:
    item = {}
    item['href'] = li.xpath('./a/@href')[0] if li.xpath('./a/@href') != [] else ''
    item['text'] = li.xpath('./a/text()')[0] if li.xpath('./a/text()') != [] else ''
    print(item)