# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午3:14 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver')

driver.get('http://www.baidu.com')

time.sleep(2)
# 输入python
kw_element = driver.find_element_by_id('kw')
kw_element.send_keys('python')

time.sleep(2)
# 点击 百度一下
su_element = driver.find_element_by_id('su')
su_element.click()

input(222)
# element.send_keys()
# element.click()

"""常用的属性和方法"""
# driver.save_screenshot() 截图
# driver.title # 当前标签页的标题文本内容
print(driver.current_url) # 当前的url
print('='*10)
print(driver.page_source) # 网页的源代码(加载完毕或加载中的)
print('='*10)
print(driver.get_cookies()) # 当前标签页的cookies list

driver.quit()

