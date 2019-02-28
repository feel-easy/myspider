# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午3:49 GMT+8

# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午3:17 GMT+8


# url_list
# 遍历 发送请求 获取响应
# 分组提取数据
# 保存数据

import requests
from lxml import etree
from queue import Queue
from threading import Thread


class QiushiSpider():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }
        self.url_q = Queue() # url队列
        self.html_q = Queue() # 响应内容队列
        self.items_q = Queue() # 数据队列

    def get_url_list(self):
        """构造url,put进url_q队列中"""
        for i in range(1,14):
            self.url_q.put('https://www.qiushibaike.com/8hr/page/{}/'.format(i))

    def get_html(self):
        """不断 从url队列中取出一个url,发送请求,获取响应,把响应内容放入html_q队列"""
        while True:
            url = self.url_q.get()
            resp = requests.get(url, headers=self.headers)
            self.html_q.put(resp.text)
            self.url_q.task_done() # 计数 -1

    def get_items(self):
        """不断 从html_q队列中取出一页的html_str,提取数据,构造数据列表,放入数据队列中"""
        while True:
            html_str = self.html_q.get()
            html = etree.HTML(html_str)
            div_list = html.xpath('//div[@id="content-left"]/div')
            # print(len(div_list))
            result_list = []
            for div in div_list:
                item = {}
                item['name'] = div.xpath('.//h2/text()')[0]
                item['content'] = div.xpath('.//div[@class="content"]/span/text()')
                # print(item)
                result_list.append(item)
            self.items_q.put(result_list)
            self.html_q.task_done()

    def save_results(self):
        """不断从数据队列中取出一页数据,分别保存"""
        while True:
            result_list = self.items_q.get()
            for item in result_list:
                print(item)
            self.items_q.task_done()

    def run(self):
        """爬虫运行逻辑"""

        # url_q
        self.get_url_list()

        # 构造线程列表
        t_list = []

        # 用线程去执行各个函数
        for i in range(5):
            t_html = Thread(target=self.get_html)
            t_list.append(t_html)

        for i in range(3):
            t_parse = Thread(target=self.get_items)
            t_list.append(t_parse)

        t_save = Thread(target=self.save_results)
        t_list.append(t_save)

        # 设置守护线程,让线程执行
        for t in t_list:
            t.setDaemon(True) # 设置守护线程:主线程结束,子线程随之结束
            t.start()

        # 主线程调用q队列的join函数,来阻塞
        for q in [self.url_q, self.html_q, self.items_q]:
            q.join() # 阻塞当前的主线程,直到q的计数为0

        print('程序结束!')


if __name__ == '__main__':
    import time

    start = time.time()
    spider = QiushiSpider()
    spider.run()
    print('耗时:{}秒'.format(time.time() - start))
    # 单线程 耗时: 4.90
    # 多线程 耗时: 1.16

