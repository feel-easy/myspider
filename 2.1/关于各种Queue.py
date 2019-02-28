# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-16 下午6:10 GMT+8


from queue import Queue
from multiprocessing.dummy import Queue
from multiprocessing.dummy import JoinableQueue
# 以上三个都是queue.Queue

from multiprocessing import Queue # 跨进程的Queue
from multiprocessing import JoinableQueue # 就是multiprocessing.Queue多了join和task_done方法

from multiprocessing import SimpleQueue # 只有empty get put 方法

