# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from helper.DbHelper import DButil

class DoubanbookPipeline(object):
    db = DButil()
    # items = []
    def process_item(self, item, spider):
        # con = json.dumps(dict(item)).encode('utf-8') + '\n'
        # self.items.append(item)
        self.db.save_mysql('book', item)
        return item
