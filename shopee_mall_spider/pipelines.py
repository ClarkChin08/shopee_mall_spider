# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MallShopDownloadPipeline(object):
    
    def __init__(self, db_uri, db_port):
        self.db_uri = db_uri
        self.db_port = db_port
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                crawler.settings.get("MongoDB_URI"),
                crawler.settings.get("MongoDB_PORT")
            )
        
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.db_uri, port=self.db_port)
        
    def process_item(self, item, spider):
        db_name = item.get('crawl_country')
        collection_name = item.get("crawl_data_type")
        if collection_name:
            self.client[db_name][collection_name].insert_one(item)
            

        
        
    def close_spider(self, spider):
        self.client.close()






