# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午4:57 GMT+8

import traceback
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')
driver.get("https://www.baidu.com")

try:
    driver.find_element_by_xpath('//hahah')
except:
    print(traceback.format_exc())
finally:
    driver.quit()