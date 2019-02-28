# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午3:17 GMT+8


# url_list
# 遍历 发送请求 获取响应
# 分组提取数据
# 保存数据

import requests
from lxml import etree


class QiushiSpider():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }

    def get_url_list(self):
        # url_list
        return ['https://www.qiushibaike.com/8hr/page/{}/'.format(i)
                for i in range(1,14)]

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

    def run(self):
        """爬虫运行逻辑"""

        # url_list
        url_list = self.get_url_list()
        # 遍历 发送请求 获取响应
        for url in url_list:
            html_str = self.get_html(url)
            # 提取数据
            result_list = self.get_items(html_str)
            # 保存数据
            self.save_results(result_list)


if __name__ == '__main__':

    import time
    start = time.time()
    spider = QiushiSpider()
    spider.run()
    print('耗时:{}秒'.format(time.time()-start))
    # 单线程 耗时: 4.90

