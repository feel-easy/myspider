# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午4:22 GMT+8

# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午3:17 GMT+8


# url_list
# 遍历 发送请求 获取响应
# 分组提取数据
# 保存数据

import requests
from lxml import etree

from queue import Queue
from multiprocessing.dummy import Pool


class QiushiSpider():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }
        self.pool = Pool(8)
        self.url_q = Queue()
        self.total_response_nums = 0
        self.total_url_nums = 0
        self.is_running = True

    def get_url_list(self):
        # url_q
        for i in range(1,14):
            self.url_q.put('https://www.qiushibaike.com/8hr/page/{}/'.format(i))
            self.total_url_nums += 1 # url总数 +1

    def get_html(self, url):
        # 发送请求,返回响应内容
        resp = requests.get(url, headers=self.headers)
        return resp.text

    def get_items(self, html_str):
        # 分组提取数据,并返回
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
        return result_list

    def save_results(self, result_list):
        # 对一页中的所有数据进行保存
        for item in result_list:
            print(item)

    def excute_requests_items_save(self):
        url = self.url_q.get()
        html_str = self.get_html(url)
        result_list = self.get_items(html_str)
        self.save_results(result_list)

        self.total_response_nums += 1

    def _callback(self, xxxx):
        if self.is_running:
            self.pool.apply_async(self.excute_requests_items_save, callback=self._callback)

    def run(self):
        """爬虫运行逻辑"""

        # 构造url队列
        self.get_url_list()

        for i in range(8):
            # 调用线程池中的线程,异步的去处理每一个url,直到处理完毕
            self.pool.apply_async(func=self.excute_requests_items_save, callback=self._callback)

        # 退出程序的条件: 响应总数>=url总数
        while True:
            if self.total_response_nums >= self.total_url_nums:
                self.is_running = False
                break
        print('程序结束')


if __name__ == '__main__':

    import time
    start = time.time()
    spider = QiushiSpider()
    spider.run()
    print('耗时:{}秒'.format(time.time()-start))
    # 单线程 耗时: 4.90
    # 线程池 耗时: 2.78

