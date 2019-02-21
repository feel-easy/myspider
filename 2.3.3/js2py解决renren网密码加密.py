# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-19 下午5:20 GMT+8

import requests
import js2py
import json

username = '账号'
password = 'mimazifuchuan'

s = requests.session()
s.headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

# 加密之后的密码

# 获取上边js执行过程中用到的三个Js文件中的js代码
# url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js'
# resp = s.get(url)
# with open('RSA.js', 'w') as f:
#     f.write(resp.text)
# url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'
# resp = s.get(url)
# with open('BigInt.js', 'w') as f:
#     f.write(resp.text)
# url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'
# resp = s.get(url)
# with open('Barrett.js', 'w') as f:
#     f.write(resp.text)

# 发送请求获取参数n t rkey
url = 'http://activity.renren.com/livecell/rKey'
resp = s.get(url)
rkey = json.loads(resp.text)['data']['rkey']
n = json.loads(resp.text)['data']

# 实例化js执行环境(js解释器)
context = js2py.EvalJs()

# 向js执行环境中传入所需的变量
context.n = n
context.t = {'password': password}

# 向js执行环境中添加js代码,并执行
with open('RSA.js', 'r') as f:
    context.execute(f.read())
with open('BigInt.js', 'r') as f:
    context.execute(f.read())
with open('Barrett.js', 'r') as f:
    context.execute(f.read())

js_str = """
t.password = t.password.split("").reverse().join(""),
setMaxDigits(130);
var o = new RSAKeyPair(n.e,"",n.n)
  , r = encryptedString(o, t.password);"""

context.execute(js_str)

# 取出js执行环境中某个变量的值
password = context.r

print(password)

# 登录post url
# url = ''
# data = {}