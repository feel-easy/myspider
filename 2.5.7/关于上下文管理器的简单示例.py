# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-25 下午6:15 GMT+8



# 上下文管理器的原理: 在最后能够正确的回收资源
# f = open('xxx.haha', 'w')
# try:
#     f.write('sss')
#     # do otherthing
# finally:
#     f.close()



class ContextManager(object):
    def __init__(self):
        self.entered = False
    def __enter__(self):
        self.entered = True
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False


cm = ContextManager()
print(cm.entered) # False
with cm:
    print(cm.entered) # True
print(cm.entered) # False
with ContextManager() as cm:
    print(cm.entered) # True