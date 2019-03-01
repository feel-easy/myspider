import logging
import random

from ershouche.settings import IPPOOL
from ershouche.settings import UAPOOL

class MYIPPOOL(object):
    logger = logging.getLogger(__name__)
    def __init__(self,ip=''):
        self.ip = ip
    def process_request(self,request,spider):
        thisip = random.choice(IPPOOL)
        self.logger.debug('Using IP')
        print("当前使用的IP是:"+thisip['ipaddr'])
        request.meta['proxy'] = 'http://'+thisip['ipaddr']

class UserAgentMiddleware(object):
    logger = logging.getLogger(__name__)
    def __init__(self,ua=''):
        self.ua = ua
    def process_request(self,request,spider):
        thisua = random.choice(UAPOOL)
        self.logger.debug('Using Agent')
        print("当前使用的UA是:"+thisua)
        request.headers.setdefault('User-Agent',thisua)
