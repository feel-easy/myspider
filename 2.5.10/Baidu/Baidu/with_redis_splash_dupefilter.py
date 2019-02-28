# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-28 下午4:04 GMT+8

from copy import deepcopy
from scrapy.utils.request import request_fingerprint
from scrapy.utils.url import canonicalize_url
from scrapy_splash.utils import dict_hash
from scrapy_redis.dupefilter import RFPDupeFilter


def splash_request_fingerprint(request, include_headers=None):
    fp = request_fingerprint(request, include_headers=include_headers)
    if 'splash' not in request.meta:
        return fp
    splash_options = deepcopy(request.meta['splash'])
    args = splash_options.setdefault('args', {})
    if 'url' in args:
        args['url'] = canonicalize_url(args['url'], keep_fragments=True)

    return dict_hash(splash_options, fp)


class SplashAwareDupeFilter(RFPDupeFilter):
    def request_fingerprint(self, request):
        return splash_request_fingerprint(request)