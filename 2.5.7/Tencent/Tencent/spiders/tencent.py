# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    # 继承爬虫类:scrapy.spiders.CrawlSpider
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    # 多了rules规则元祖
    # crawlspider爬虫不能写名为parse的函数
    # parse函数用来实现rules规则元祖的部分功能

    rules = (
        # Rule(LinkExtractor(allow=r'Items/')),
            # LinkExtractor链接提取器,是Rule中固定参数
            # 按照链接提取器规则参数提取url,构造request;框架发送请求获取响应
        # Rule(LinkExtractor(allow=r'Items/'), follow=True),
            # 按照链接提取器规则参数提取url,构造request;框架发送请求获取响应
            # 链接提取器提取的url对应的响应,会继续进入rules规则元祖中进行处理
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item'),
            # 按照链接提取器规则参数提取url,构造request;框架发送请求获取响应
            # 链接提取器提取的url对应的响应,会进入callback指定的回调函数中进行解析
            # callback接收的是解析函数名的字符串
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
            # 按照链接提取器规则参数提取url,构造request;框架发送请求获取响应
            # 该响应即会进入callback指定的回调函数中进行解析
            # 该响应也会进入rules规则集合中被提取处理
        # 关于LinkExtractor链接提取器中的规则参数
            # allow:正则匹配a标签中href属性的值
            # deny:排除正则匹配href属性的值的a标签的url
            # allow_domains:list,按照域名进行提取
            # deny_domains:list,排除规定的域名的url
            # restrict_xpaths:xpath规则定位某个标签,该标签内的所有url都会被提取
            # 多个规则参数共同作用于结果:链接提取器最终提取的url一定是符合所有规则参数的!

        # 提取处理列表页
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), follow=True),

        # 提取处理详情页
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_detail'),

    )

    def parse_detail(self, response):
        item = {}
        item['title'] = response.xpath('//td[@id="sharetitle"]/text()').extract_first()
        item['content'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        return item

