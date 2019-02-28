# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time
from selenium import webdriver


def getCookies():
    """使用selenium获取cookies并返回"""
    user = input('请输入账号:')
    pwd = input('请输入账号:')
    # 实例化无界面driver
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver',
                              chrome_options=option)
    driver.get('https://github.com/login')

    # 输入账号密码点击登录
    time.sleep(2)
    driver.find_element_by_id('login_field').send_keys(user)
    time.sleep(2)
    driver.find_element_by_id('password').send_keys(pwd)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@name="commit"]').click()
    time.sleep(2)

    # 获取cookies_dict并返回
    cookeis_list = driver.get_cookies()
    cookies_dict = {cookie['name']:cookie['value'] for cookie in cookeis_list}

    driver.quit() # 别忘了!
    return cookies_dict


class SendCookiesDict():
    def process_request(self, request, spider):
        # 给request的cookies赋值!
        request.cookies = getCookies()