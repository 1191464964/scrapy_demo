# -*- coding: utf-8 -*-

# Scrapy settings for DoubanBook project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DoubanBook'

SPIDER_MODULES = ['DoubanBook.spiders']
NEWSPIDER_MODULE = 'DoubanBook.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DoubanBook (+http://www.yourdomain.com)'
USER_AGENT = 'doubanbook (+http://www.yourdomain.com)' \
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# Obey robots.txt rules # 爬虫是否遵循网站的协议
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)  # 请求的并发量，默认16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3    # 下载延迟 等待3秒
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16  # 爬取网站允许的域的个数
# CONCURRENT_REQUESTS_PER_IP = 16  # 爬取请求的ip允许16个

# Disable cookies (enabled by default) # 是否启用cookie
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)  # 是否启用一个爬虫监控
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:  # 默认的一个请求报头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares   # 爬虫中间键（处理爬虫和引擎之间的中间键）
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'DoubanBook.middlewares.DoubanbookSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares    # 下载中间键（请求发出去之后，引擎和下载器之间的一个处理（值越小优先级越高）
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'DoubanBook.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions   # 配置监控
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines  # 管道文件
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'DoubanBook.pipelines.DoubanbookPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
