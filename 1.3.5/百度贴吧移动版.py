# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-14 下午5:39 GMT+8

"""帖子的标题，连接和帖子中图片的链接
# 确定数据结构
{
    title
    url
    img_url = [
        img_url_1,
        img_url_2,
        ...
    ]
}

# 1. 确定某个贴吧的start_url
https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={贴吧名字}&lp=5011&lm=&pn=0
# 2. 列表页 发送请求获取响应
# 3. 分组提取 每个帖子的title和url
    # a. 详情页, 发送请求获取响应
    # b. 提取img_list
    # c. 获取详情页的下一页的url, 重复步骤a
    # 组装数据???!!!
# 4. 获取下一页的url, 重复步骤2
"""
import requests
from lxml import etree


class TiebaSpider():

    def __init__(self, spider_name, page=0):
        self.start_url = 'https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=5011&lm=&pn=0'.format(spider_name)
        self.base_url = 'https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        self.page = page

    def _get_html(self, url):
        """发送请求获取响应,返回可以xpath的html"""
        resp = requests.get(url, headers=self.headers)
        return etree.HTML(resp.content)

    def _get_img_list(self, detail_url, img_list):
        """获取一个帖子中全部的图片的url"""
        # a. 详情页, 发送请求获取响应
        detail_html = self._get_html(detail_url)
        # b. 提取img_list
        img_list += detail_html.xpath('//img[@class="BDE_Image"]/@src')
        # c. 获取详情页的下一页的url, 重复步骤a
        next_detail_href = detail_html.xpath('//a[text()="下一页"]/@href')
        if next_detail_href != []:
            next_detail_url = self.base_url + next_detail_href[0]
            self._get_img_list(next_detail_url, img_list)
        return img_list

    def _excute_item(self, item):
        """处理或保存数据"""
        print(item)

    def _get_div_list(self, html):
        """对一个列表页进行分组"""
        return html.xpath('/html/body/div[1]/div')[1:21]

    def _get_item(self, div):
        """提取一个帖子的全部数据"""
        # 组装数据
        item = {}
        item['title'] = div.xpath('./a/text()')[0]
        item['detail_url'] = self.base_url + div.xpath('./a/@href')[0]
        # 获取该帖子的全部的图片的url!
        item['img_list'] = self._get_img_list(item['detail_url'], img_list=[])
        # 处理或保存数据
        self._excute_item(item)

    def _get_next_list_href(self, html):
        """获取列表页下一页的href_list 有可能是 []"""
        return html.xpath('//a[text()="下一页"]/@href')


    def _main(self):
        """爬虫运行逻辑"""
        # 1. 确定某个贴吧的start_url
        next_list_url = self.start_url
        i = 0
        while i < self.page:
            # 2. 列表页 发送请求获取响应
            html = self._get_html(next_list_url)
            # 3. 分组提取 每个帖子的title和url
            div_list = self._get_div_list(html)
            # print(len(div_list))
            for div in div_list:
                # 提取一个帖子的全部数据
                self._get_item(div)
            # 4. 获取下一页的url, 重复步骤2
            next_list_href = self._get_next_list_href(html)
            if next_list_href != []:
                next_list_url = self.base_url + next_list_href[0]
            else:
                break

            if self.page != 0:
                i += 1
            else:
                i -= 1

    def run(self):
        self._main()



if __name__ == '__main__':
    spider = TiebaSpider('lol', page=2)
    spider.run()