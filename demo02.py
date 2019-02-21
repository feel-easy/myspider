import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://www.baidu.com/")
# print(driver.page_source)
# time.sleep(4)
driver.find_element_by_id('kw').send_keys('python')
# time.sleep(4)
driver.find_element_by_id('su').click()
print(driver.get_cookies())
time.sleep(6)
driver.quit()