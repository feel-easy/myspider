# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-2 下午12:10 GMT+8

import time

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
import js2py


class SinaGunDong(Spider):

    name = "sina"

    timed_task = True # 有人认为下边写个while就不用声明timed_task变量为True了，你改成False试试！

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "UOR=www.google.com,www.sina.com.cn,; SGUID=1520816292777_83076650; SINAGLOBAL=211.103.136.242_1520816292.736990; SUB=_2AkMt-V_2f8NxqwJRmPEQy2vmZYx_zwjEieKbpa4tJRMyHRl-yD83qnIJtRB6BnlxGSLw2fy6O04cZUKTsCZUeiiFEsZE; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhpFUZmqbYYLueonGrZIL2c; U_TRS1=0000001a.e268c0.5aaa0d39.35b0731a; lxlrttp=1521688012; Apache=223.72.62.219_1522208561.132697; ULV=1522208952476:6:6:3:223.72.62.219_1522208561.132697:1522208561158; U_TRS2=000000db.81c2323e.5abca69b.ad269c11; ArtiFSize=14; rotatecount=1; hqEtagMode=1",
        # "Host": "roll.news.sina.com.cn",   这里host必须禁用掉
        "Pragma": "no-cache",
        "Referer": "http://roll.news.sina.com.cn/s/channel.php?ch=01",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }

    def start_requests(self):
        while True:
            # 需要发起这个请求，才能获取到列表页数据，并且返回的是一个js语句
            url = "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&spec=&type=&ch=&k=&offset_page=0&offset_num=0&num=120&asc=&page=1&r=0.5559616678192825"
            yield Request(url, parse='parse', filter=False)
            time.sleep(60)     # 每60秒发起一次请求

    def parse(self, response):
        print(response.body)
        '''响应体数据是js代码'''
        # 使用js2py模块，执行js代码，获取数据
        ret = js2py.eval_js(response.body.decode("gbk"))    # 对网站分析发现，数据编码格式是gbk的，因此需要先进行解码
        for news in ret.list:    #
            yield Request(news["url"], headers=self.headers, parse='parse_detail', meta={"type": news["channel"]["title"]})

    def parse_detail(self, response):
        # print(response.body)
        response.body = response.body.decode("utf-8")    # 部分页面无法正确解码，因此在这里手动进行解码操作
        title = response.xpath("//h1[@class='main-title']/text()")[0]
        pub_date = response.xpath("//span[@class='date']/text()")[0]
        try:
            author = response.xpath("//div[@class='date-source']//a/text()")[0]    # 由于作者的提取，有两种格式，因此这里使用一个异常捕获来进行判断
        except IndexError:
            author = response.xpath("//div[@class='date-source']//span[contains(@class,'source')]/text()")[0]
        content = response.xpath("//div[@class='article']//text()")    # 多个  每一个代表一段
        image_links = response.xpath("//div[@class='article']//img/@src")    # 图片链接有多个

        item = {
            "content": content,    # 正文
            "image_links":image_links,    # 图片链接
            "title": title,    # 标题
            "pub_date":pub_date,    # 发布日期
            "author": author,    # 作者
            "url": response.url,    # 文章链接
            "type": response.meta["type"],    # 文章所属分类
        }

        print(item)
        yield item