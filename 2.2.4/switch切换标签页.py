# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午4:21 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../chromedriver')
driver.get("https://www.baidu.com/")

time.sleep(2)

# 通过执行js来新开一个标签页
js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)

print(driver.current_url)

"""switch_to切换标签页"""
windows_list = driver.window_handles # 标签页id_name构成的list

driver.switch_to.window(windows_list[1])
print(driver.current_url)
time.sleep(2)

driver.switch_to.window(windows_list[0])
print(driver.current_url)
time.sleep(2)

driver.quit()