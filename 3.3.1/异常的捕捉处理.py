# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午5:49 GMT+8

import logging

# try:
#     print(1+'1')
# except Exception as e:
#     print(e)


# try:
#     raise Exception("异常")
# except Exception as e:
#     logging.exception(e)


import traceback

try:
    raise Exception("异常")
except:
    print(traceback.format_exc())
    logging.error(traceback.format_exc())