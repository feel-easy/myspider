# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['xxx']
    start_urls = ['https://github.com/1596930226'] # 这个起始的url需要登陆后/携带cookie才能获取

    def start_requests(self):
        """构造request,携带cookie,并返回"""
        cookies_str = '_ga=GA1.2.302602793.1531037036; _octo=GH1.1.841735624.1531037036; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; user_session=treJFNCxdIw3iW0GH3aZlOv8ZnJ93-B9VB498jPLT4uyTsu_; __Host-user_session_same_site=treJFNCxdIw3iW0GH3aZlOv8ZnJ93-B9VB498jPLT4uyTsu_; logged_in=yes; dotcom_user=1596930226; _gh_sess=dWVINkd4ZDA0ZGkyZkNjQ01vNUFyQWZNQklLNnRjTHFCOHBBQ0pZYkFwRmEzZlFER0ZvazFISnVQVTlhM2l2YUduUDYyQTkzZUp3eVc1eFFhZnExVXV0SVFWSUxITFBNd2toUzAyVjZidW0rS1JIbWlNU3ViUE15bERFZ05Ua3E0ZGFoVFlhMHdkUmNjSkFmREtKQ2pDU1dRaldZRXlXcXFubW5RNWN4NUF3aC9idXFFN0FjRG92TE1SVTFoQmUxLS1CT1cxTjJlZmp4QWFVM1h4YnIyazNRPT0%3D--0961bd450ea1c72175f92f42b825ccbab2c66294'
        cookies_dict = {cookie.split('=')[0]:cookie.split('=')[1]
                        for cookie in cookies_str.split('; ')}

        yield scrapy.Request(self.start_urls[0],
                             cookies=cookies_dict,
                             callback=self.parse)

    def parse(self, response):
        with open('login1.html', 'w') as f:
            f.write(response.body.decode())
