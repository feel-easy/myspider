# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午5:02 GMT+8
import time

from selenium import webdriver

"""开启Chromedriver无界面模式"""
option = webdriver.ChromeOptions()
# option.add_argument('--headless') # 使用无头模式
# option.add_argument('--disable-gpu') # 禁止显卡

"""替换UA"""
option.add_argument('--user-agent=UA_STR')

"""使用代理ip"""
option.add_argument('--proxy-server=https://119.102.24.23:9999')

driver = webdriver.Chrome(executable_path='../chromedriver',
                          chrome_options=option)
driver.get("https://www.baidu.com")
time.sleep(2)
print(driver.title)
driver.quit()