# -*- coding: utf-8 -*-
import scrapy
# 从哪里执行 就从哪里导包!
from Tencent.items import TencentItem


class Tencent2Spider(scrapy.Spider):
    name = 'tencent2'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 提取数据
        tr_list = response.xpath('//table[@class="tablelist"]//tr')[1:-1]
        for tr in tr_list:
            title = tr.xpath('.//a/text()').extract_first()
            # 获取详情页的url构造request,指定callback解析函数并返回
            detail_url = 'https://hr.tencent.com/' + tr.xpath('.//a/@href').extract_first()
            yield scrapy.Request(detail_url,
                                 callback=self.parse_detail,
                                 meta={'title':title}) # 给callback指定函数传递meta字典

        # 翻页
        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_href != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_href
            """构造并返回request"""
            yield scrapy.Request(next_url, callback=self.parse)


    def parse_detail(self, response):
        # response.meta == response.request.meta == request.meta == {'title':title}
        # 取出meta传递的数据
        # title = response.meta['title']
        # 组装数据
        item = TencentItem() # 实例化baseitem类
        # 实例化后当字典一样使用
        item['title'] = response.meta['title']
        item['content'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        yield item # {} BaseItem Request None
