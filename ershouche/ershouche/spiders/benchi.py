# -*- coding: utf-8 -*-
import time
from random import randint

import scrapy

from ershouche.items import ErshoucheItem


class BenchiSpider(scrapy.Spider):
    name = 'benchi'
    allowed_domains = ['xin.com']
    start_urls = ['https://www.xin.com/benchi']

    def parse(self, response):
        for ershouche_item in response.xpath('//div[@class="pad"]'):
            item = {
                'name': ershouche_item.xpath('./h2/span/text()').extract_first().strip(),
                'url': "https:{}".format(ershouche_item.xpath('./h2/span/@href').extract_first().strip()),
                'start_year': ershouche_item.xpath('./span/text()').extract_first().replace(" ", "").replace("\n", ""),
                'price': "{}".format(
                    ershouche_item.xpath('./p/em/text()').extract_first().replace(" ", "").replace("\n", "")),

            }
            detail_url = "https:{}".format(ershouche_item.xpath('./h2/span/@href').extract_first().strip())

            yield scrapy.Request(detail_url,
                                 callback=self.parse_detail,
                                 meta=item) # 给callback指定函数传递meta字典
        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_href:
            next_url = 'https://www.xin.com' + next_href
            yield scrapy.Request(next_url, callback=self.parse)


    def parse_detail(self,response):
        time.sleep(randint(1, 3))
        item = ErshoucheItem()
        last_item = response.meta
        item['name'] = last_item['name']
        item['start_year'] = last_item['start_year']
        item['price'] = last_item['price']
        item['content_url'] = "https:{}".format(response.xpath("//img[@class='cd_m_info_mainimg']/@src").extract_first())
        item['info'] = response.xpath("//div[@class='cd_m_info_it2']/p/span[@class='cd_m_info_qgzg']/span[@class='p-storage']/text()").extract_first()
        yield item

