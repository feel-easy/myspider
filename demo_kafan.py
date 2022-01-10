import requests
from lxml import etree
import json
# import pymysql

# mysql_conf = {
#         "host": '127.0.0.1',
#         "port": 3306,
#         "user": 'root',
#         "password": 'root',
#         "db": 'questions',
#         "charset": "utf8",
#         "cursorclass": pymysql.cursors.DictCursor
#     }
 
# conn = pymysql.connect(**mysql_conf)


def fetchHtml(_url):
  _resp = requests.get(_url)
  return etree.HTML(_resp.content)

def toText(el):
  return ''.join([i for i  in el.itertext()])

def findRet(_elems, _text):
  return ';'.join([i for i in _elems if i.count(_text)]).strip()

def toJson(_html):
  _tmps = map(toText, _html.xpath('//p'))
  _elems = [i for i in _tmps]
  return {
    "question": findRet(_elems, '问题：'),
    "options": findRet(_elems, '选项：'),
    "result": findRet(_elems, '答案：')
  }

if __name__ == '__main__':
  url = 'https://www.kafan.cn/edu/22214241.html'
  # resp = requests.get(url)
  html = fetchHtml(url)
  urls = html.xpath('//p/a[2]/@href')
  results = []
  for _url in urls:
  # _url = urls[0]
    _html = fetchHtml(_url)
    _ret = toJson(_html)
    if _ret["question"] and _ret["options"] and _ret["result"]:
      print(_ret)
      results.append(_ret)
  with open('result.json', 'w') as f:
    f.write(json.dumps({'问题答案':results}, ensure_ascii=False))
  
  