# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

from lxml import etree


class Response():

    def __init__(self, url=None, headers=None, status_code=None, body=None):

        self.url = url
        self.headers = headers
        self.status_code = status_code
        self.body = body


    def xpath(self, xpath_str):
        html = etree.HTML(self.body)
        return html.xpath(xpath_str)