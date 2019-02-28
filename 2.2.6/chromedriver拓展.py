# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午5:02 GMT+8

from selenium import webdriver

"""开启Chromedriver无界面模式"""
option = webdriver.ChromeOptions()
option.add_argument('--headless') # 使用无头模式
option.add_argument('--disable-gpu') # 禁止显卡

"""替换UA"""
option.add_argument('--user-agent=UA_STR')

"""使用代理ip"""
option.add_argument('--proxy-server=https://192.168.22.55:9527')

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver',
                          chrome_options=option)
driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()