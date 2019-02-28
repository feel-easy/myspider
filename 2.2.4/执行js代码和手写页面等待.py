# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午4:03 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver')

driver.get('https://www.taobao.com')

"""手动实现页面等待: 不断去判断某个标签是否存在"""
i = 0
while 1:
    i += 1
    # js = '让浏览器向下滚动一定px'
    js = 'document.documentElement.scrollTop={}'.format(i*500)
    try:
        """driver调用浏览器执行js代码"""
        driver.execute_script(js)
        time.sleep(2)
        # 定位淘宝淘抢购的a标签
        a = driver.find_element_by_xpath('//div[@class="qiang-inner"]/h3[1]/a[1]')
        href = a.get_attribute('href')
        print(href)
        driver.quit()
        break
    except:
        print('none')

"""selenium页面等待:
    强制等待 sleep
    隐式等待
    显式等待
    手写页面等待
"""