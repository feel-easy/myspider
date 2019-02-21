import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get('https://www.baidu.com/')
print(driver.page_source)

print(driver.get_cookies())
print(driver.current_url)
time.sleep(6)
driver.quit()