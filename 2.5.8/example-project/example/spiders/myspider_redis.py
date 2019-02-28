from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    # start_urls = ['https://jd.com']
    redis_key = 'myspider:start_urls'
    # allowed_domains = ['jd.com', 'p.3.cn']

    def __init__(self, *args, **kwargs):
        # {'domain': 'jd.com,p.3.cn'}
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
