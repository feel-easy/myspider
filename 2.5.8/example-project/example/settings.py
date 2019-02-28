# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

REDIS_URL = 'redis://127.0.0.1:6379'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter" # 将request转换为指纹
SCHEDULER = "scrapy_redis.scheduler.Scheduler" # request调度器
SCHEDULER_PERSIST = True # 表示是否持久化request队列和request指纹
# SCHEDULER_PERSIST为True 程序结束时不删除request的队列和指纹集合
# SCHEDULER_PERSIST为False 程序结束时会删除request的队列和指纹集合

#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400, # 把Item存入redis
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1


