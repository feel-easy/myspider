# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫名
    allowed_domains = ['itcast.cn'] # 允许爬取范围的域名,可以是多个
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 起始url的list,可以是多个
    # start_urls列表中的url不受allowed_domains的限制

    # scrapy.Spider类爬虫都必须有名为parse的解析函数!
    def parse(self, response):
        # 专门解析每个start_url对应的响应
        """响应的response对象的常用属性"""
        # print(response.body) # 响应内容 bytes
        # print(response.url) # 响应url
        # print(response.headers) # 响应的headers
        # print(response.request.headers) # 响应对应的请求头
        # print(response.status) # 状态吗 int

        # 先分组 再提取
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            name = li.xpath('.//h3/text()') # 返回由selector对象构成类list
            name = li.xpath('.//h3/text()').extract() # 返回字符串构成的list
            name = li.xpath('.//h3/text()').extract_first() # 返回列表中第一个字符串
            # print(name)
            # 组装数据
            item = {}
            item['name'] = name

            yield item
