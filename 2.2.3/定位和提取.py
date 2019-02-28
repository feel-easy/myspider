# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午3:43 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver')

driver.get('https://www.douban.com/')

"""定位的方法driver.find_element(s)"""
# 定位方法 只能定位标签对象
# ret1 = driver.find_element_by_id("anony-nav")
# print(ret1)
# ret1 = driver.find_elements_by_id("anony-nav")
# print(ret1)

# by_xpath()只能定位标签,不能在xpath_str写提取属性值或提取文本内容!!!
# ret3 = driver.find_elements_by_xpath("//*[@id='anony-nav']/h1/a")
# print(ret3)

# ret4 = driver.find_elements_by_tag_name("h1")
# print(len(ret4))

ret5 = driver.find_elements_by_link_text("下载豆瓣 App")
print(len(ret5))

ret6 = driver.find_elements_by_partial_link_text("豆瓣")
print(len(ret6))

"""
提取文本内容element.text
属性值get_attribute()的方式"""
content = ret5[0].text
print(content)

for ret in ret6:
    print(ret.get_attribute('href'))

driver.quit()