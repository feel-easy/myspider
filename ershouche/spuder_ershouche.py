# _*_ coding:utf-8 _*_
import random

import requests
import time
from lxml import etree
from random import randint
import faker

cookies_str = "XIN_anti_uid=3CEFA6D9-A446-B367-E80C-D7E5832CD906; path=/; domain=.www.xin.com; Expires=Sat, 02 Mar 2019 06:25:40 GMT;"
# 构造cookies_dict
cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1]
                for cookie in cookies_str.split('; ')}


def getcookies_dict(cookies_str):
    return {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_str.split('; ')}


def get_header():
    f = faker.Faker(locale='zh_CN')
    ua = f.chrome()
    return {
        'User-Agent': ua,
        'Referer': "https://www.xin.com/",
    }


def get_proxies():
    ips = ['58.243.204.218:4243','60.162.228.83:4247','112.252.68.109:4274','115.221.8.176:2316','220.165.154.167:4232','115.85.206.163:3012','125.64.124.154:4286','106.111.45.131:1649','115.225.175.49:2314','220.188.12.159:4256']
    proxies = {
        'https': 'https://{}'.format(random.choice(ips))
    }
    print(proxies)
    return proxies


def get_request(url):
    print(url)
    try:
        response = requests.get(url=url, headers=get_header(), proxies=get_proxies())
        # response.enconding = 'utf-8'
        text = response.text
        print(response.status_code)
    except:
        text = '<img class="cd_m_info_mainimg" src="" onclick="uxl_track(\'w_vehicle_details/top_pic/carid/74027596\');">'

    # cookies_dict1 = requests.utils.dict_from_cookiejar(response.cookies)

    # print(cookies_dict1)


    # print(text)
    return text


def spider_list(text):
    root = etree.HTML(text)
    name_list = root.xpath('//div[@class="pad"]//h2/span/text()')
    url_list = root.xpath('//div[@class="pad"]//h2/span/@href')
    data = []
    for i in range(len(name_list)):
        # time.sleep(randint(1, 3))
        url = "https:{}".format(url_list[i])

        data.append(str({
            "name": name_list[i],
            "content_data": get_content(url)
        }))
        # print(data)
    # saveData(data)


def saveData(data):
    with open("data.data", "w", encoding="utf-8") as f:
        f.writelines(data)


def get_data(url_list):
    for i in url_list:
        get_content(i)


def get_content(url):
    root = etree.HTML(get_request(url))
    img_url = root.xpath("//img[@class='cd_m_info_mainimg']/@src")
    print(img_url)
    return {
        'img_url': img_url
    }


def spader_main():
    start_url = 'https://www.xin.com/beijing/i1/'
    text = get_request(start_url)
    spider_list(text)


if __name__ == '__main__':
    spader_main()
    # url = "https://www.xin.com/9qw5jr5dr5/che74027596.html?cityid=201"
    # start_url = 'https://www.xin.com/beijing/i1/'
    # # get_request(start_url)
    # print(get_content(url))
