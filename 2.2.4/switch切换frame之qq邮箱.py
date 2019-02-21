# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午4:28 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../chromedriver')
driver.get("https://mail.qq.com")

"""切入frame标签"""
frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame) # 切换frame

try:
    # 输入账号密码点击登录
    time.sleep(2)
    driver.find_element_by_id('u').send_keys('1596930226')
    time.sleep(2)
    driver.find_element_by_id('p').send_keys('jiubugaosuni')
    time.sleep(2)
    driver.find_element_by_id('login_button').click()
    print('搞定!')
except:
    print('搞不定!')
    driver.quit()

"""切出frame标签"""
driver.switch_to.window(driver.window_handles[0])

print(driver.find_element_by_xpath('//*[@class="login_pictures_title"]').text)

input(222)
driver.quit()
