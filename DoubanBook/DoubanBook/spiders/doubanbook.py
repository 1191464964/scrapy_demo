# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.parse
from scrapy import Selector
from DoubanBook.items import DoubanbookItem
from helper.Method import delete_blank, delete_biaoqian


class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['https://book.douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%B5%81%E8%A1%8C']
    offset = 0

    def parse(self, response):
        cc = Selector(response)
        con = cc.xpath('//table[@class="tagCol"]/tbody/tr/td')
        # print(con.extract())
        for c in con:
            url = 'https://book.douban.com' + c.xpath('./a/@href').extract()[0]
            print(url)
            yield scrapy.Request(url, callback=self.parse1, dont_filter=True)

    def parse1(self, response):
        item = DoubanbookItem()
        ss = Selector(response)
        con = ss.xpath('//*[@id="subject_list"]/ul/li')
        for c in con:
            title = c.xpath('./div[2]/h2/a/text()').extract()[0]
            url = c.xpath('./div[2]/h2/a/@href').extract()[0]
            score = c.xpath('./div[2]/div[2]/span[2]/text()').extract()[0]
            CommentCount = c.xpath('./div[2]/div[2]/span[3]/text()').extract()[0]
            label = response.url.replace('https://book.douban.com/tag/', '').replace('?start=1000&type=T', '')
            item['title'] = delete_blank(title)
            item['url'] = url
            item['score'] = score
            item['CommentCount'] = re.search('\((.*?)人评价\)', CommentCount).group(1)
            item['label'] = urllib.parse.unquote(label)
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2, dont_filter=True)
            if self.offset < 980:
                self.offset += 20
                next_url = response.url + str(self.offset) + 'start=1000&type=T'
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse2(self, response):
        item = response.meta['item']
        ss = Selector(response)
        con = ss.xpath('//div[@id="info"]').extract()[0]
        con = delete_blank(con)
        author = re.search("作者(.*?):(.*?)</a>", con)
        author = delete_biaoqian(author.group(2))
        press = re.search('出版社:</span>(.*?)<br', con).group(1)
        date = re.search('出版年:</span>(.*?)<br', con).group(1)
        page = re.search('页数:</span>(.*?)<br', con).group(1) if re.search('页数:</span>(.*?)<br', con) != None else ''
        price = re.search('定价:</span>(.*?)<br', con).group(1).replace('元', '') + '元'
        isbn = re.search('ISBN:</span>(.*?)<br', con).group(1)
        item['author'] = author
        item['press'] = press
        item['date'] = date
        item['page'] = page
        item['price'] = price
        item['isbn'] = isbn
        yield item
