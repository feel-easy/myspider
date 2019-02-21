# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-19 下午4:56 GMT+8

# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-19 上午10:08 GMT+8


"""
	1. requests.session
	2. 向首页、登陆页发送请求
	3. 向图片发送请求
	4. 发送登陆请求
"""

import requests

s = requests.session()
s.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

# 登录页
url = 'http://oa.itcast.cn/seeyon/index.jsp'
s.get(url)

# 验证码
url = 'http://oa.itcast.cn/seeyon/verifyCodeImage.jpg'
resp = s.get(url)
with open('captcha.jpg', 'wb') as f:
    f.write(resp.content)

# 输入验证码
VerifyCode = input('请输入验证码:')

# 登录请求
url = 'http://oa.itcast.cn/seeyon/main.do?method=login'
data = {
    'authorization': '',
    'login.timezone': 'GMT+8:00',
    'login_username': 'yaoxiangyu@itcast.cn',
    'login_password': 'xxxxxx',
    'login_validatePwdStrength': '1',
    'login.VerifyCode': VerifyCode,
    'random': '',
    'fontSize': '12',
    'screenWidth': '1920',
    'screenHeight': '1080',
}
s.post(url, data=data)

# 登录验证
resp = s.get('http://oa.itcast.cn/seeyon/main.do?method=main')
print(resp.text)