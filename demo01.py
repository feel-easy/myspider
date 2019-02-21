from selenium import webdriver
import time
# 指定driver的绝对路径
# driver = webdriver.PhantomJS(executable_path='/home/worker/Desktop/driver/phantomjs')
driver = webdriver.Chrome(executable_path='chromedriver')
# 向一个url发起请求
driver.get("http://www.taobao.com/")
# 把网页保存为图片
time.sleep(3)
driver.save_screenshot("taobao.png")
# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！