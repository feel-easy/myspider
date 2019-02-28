import sys
import requests
import threading
import datetime

# 传入的命令行参数，要下载文件的url
# url = sys.argv[1]
url = 'http://127.0.0.1:5000'
# 自定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
# 最终保存的文件名
file_name = 'test.txt'

# 线程数
num_thread = 3

def Handler(start, end, url, filename, test_var):
    headers['Range'] = 'bytes=%d-%d' % (start, end)
    r = requests.get(url, headers=headers, stream=True) # 开启stream流模式
    # 写入文件对应位置
    # r+ 以读写方式打开文件，可对文件进行读和写操作
    with open(filename, "r+b") as fp:
        fp.seek(start) # 移动当文件第p个字节处，绝对位置
        fp_position = fp.tell() # 文件指针位置
        print('线程{}，文件指针位置{}，起始位置{}，中止位置{}，写入{}'.format(
            test_var+1, fp_position, start, end, r.content.decode()))
        fp.write(r.content)


def download_file(url, num_thread=num_thread):
    r = requests.head(url) # 用很少的流量获取响应头部信息！
    print(r.headers['content-length'])
    try: # Content-Length获得文件主体的大小
        file_size = int(r.headers['content-length'])
    except: # 当http服务器使用Connection:keep-alive时，不支持Content-Length
        print("检查URL，或不支持对线程下载")
        return

    #  创建一个和要下载文件一样大小的文件
    fp = open(file_name, "wb")
    fp.truncate(file_size) # 指定文件大小
    fp.close()

    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    print('开启{}个线程'.format(num_thread))
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part

        # 构造线程函数的参数字典
        thread_kwargs = {
            'start': start,
            'end': end,
            'url': url,
            'filename': file_name,
            'test_var': i
        }

        t = threading.Thread(target=Handler, kwargs=thread_kwargs)
        t.setDaemon(True)
        t.start()
        print('线程{}开始'.format(t.name))

    # 等待所有线程下载完成
    main_thread = threading.current_thread() # 获取主线程对象
    for t in threading.enumerate(): # 当前存在的所有线程对象的列表
        if t is main_thread:
            continue # 排除主线程
        t.join() # 主线程挨个调用子线程的 join()方法。当所调用线程都执行完毕后，才停止阻塞向下执行
        print('线程{}已完成'.format(t.name))
    print('%s 下载完成' % file_name)


if __name__ == '__main__':
    start = datetime.datetime.now().replace(microsecond=0)
    download_file(url)
    end = datetime.datetime.now().replace(microsecond=0)
    print("用时: ", end='')
    print(end - start)