# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-2 上午11:59 GMT+8

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request


class TencentSpider(Spider):

    name = 'tencent'
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response): # 对start_urls进行解析
        # with open('error.html', 'w') as f:
        #     f.write(response.body.decode())
        print(response.url + '*****')
        tr_list = response.xpath('//*[@class="tablelist"]//tr')[1:-1]
        print(len(tr_list))

        for tr in tr_list:
            item = {}
            # 获取一部分数据
            item['name'] = tr.xpath('./td[1]/a/text()')[0]
            item['address'] = tr.xpath('./td[4]/text()')[0]
            item['time'] = tr.xpath('./td[5]/text()')[0]
            # 获取详情页url,并发送请求
            detail_url = 'https://hr.tencent.com/' + tr.xpath('./td[1]/a/@href')[0]
            print(detail_url)
            yield Request(
                detail_url,
                parse='parse_detail',
                meta=item # meta接收一个字典
            )
        # 翻页
        print(response.xpath('//a[text()="下一页"]/@href')[0])
        next_url = 'https://hr.tencent.com/' + response.xpath('//a[text()="下一页"]/@href')[0]
        if response.xpath('//a[text()="下一页"]/@href')[0] != 'javascript:;':
            yield Request(next_url, parse='parse')

    def parse_detail(self, response):
        # print(response.body)
        item = response.meta # 获取传入的meta
        item['job_content'] = response.xpath('//*[@class="squareli"]//text()')[0] # 加入岗位职责数据
        print(item)
        yield item