import requests
import datetime

start = datetime.datetime.now().replace(microsecond=0)

url = '.avi'
# 自定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
s = requests.session()
s.headers = headers

resp = s.get(url, stream=True) # 开启流

f = open('./hahah.mp4', 'wb')

n = 0
# iter_content()：一块一块的遍历要下载的内容
# iter_lines()：一行一行的遍历要下载的内容
for chunk in resp.iter_content(chunk_size=4096):
    n += 1
    if chunk:
        print(n)
        f.write(chunk)

f.close()

end = datetime.datetime.now().replace(microsecond=0)
print("用时: ", end='')
print(end - start)