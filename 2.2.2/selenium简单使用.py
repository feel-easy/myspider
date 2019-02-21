# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午3:06 GMT+8

from selenium import webdriver

# 实例化driver对象
driver = webdriver.Chrome('../chromedriver')
# driver = webdriver.PhantomJS('/home/worker/Desktop/driver/phantomjs')

# 通过driver调用chromedriver,通过chromedriver去调用操作系统具有的chrome浏览器内核
driver.get('http://www.taobao.com')

# chrome浏览器>=70版本 就不能使用截图功能
# driver.save_screenshot('taobao.png')

# 关闭的是当前的标签页
driver.close()

# 关闭浏览器
driver.quit()