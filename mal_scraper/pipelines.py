# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MalScraperPipeline:
    def process_item(self, item, spider):
        return item

class AnimeDetailsPipeline():
    def __init__(self):
        self.connect = pymongo.MongoClient()
        self.db = self.connect["mal_test"]
        self.collection = self.db["anime_test"]

    def __del__(self):
        self.connect.close()

    def process_item(self, item, spider):
        item = item["json_response"]
        item["_id"] = item["mal_id"]
        try:
            self.collection.insert_one(item)
            # print(item.keys())
        except pymongo.errors.DuplicateKeyError as e:
            pass
        return item

class AnimeCharactersStaffPipeline():
    def __init__(self):
        self.connect = pymongo.MongoClient()
        self.db = self.connect["mal_test"]
        self.collection = self.db["character_test"]

    def __del__(self):
        self.connect.close()
    
    def process_item(self, item, spider):
        item = item["json_response"]
        item["_id"] = item["mal_id"]
        try:
            self.collection.insert_one(item)
        except pymongo.errors.DuplicateKeyError as e:
            pass
        return item

class AnimeStatsPipeline():
    def __init__(self):
        self.connect = pymongo.MongoClient()
        self.db = self.connect["mal_test"]
        self.collection = self.db["stats_test"]

    def __del__(self):
        self.connect.close()
    
    def process_item(self, item, spider):
        item = item["json_response"]
        item["_id"] = item["mal_id"]
        try:
            self.collection.insert_one(item)
            # print(item.keys())
        except pymongo.errors.DuplicateKeyError as e:
            pass
        return item

class AnimePicturesPipeline():
    def __init__(self):
        self.connect = pymongo.MongoClient()
        self.db = self.connect["mal_test"]
        self.collection = self.db["pictures_test"]

    def __del__(self):
        self.connect.close()
    
    def process_item(self, item, spider):
        item = item["json_response"]
        item["_id"] = item["mal_id"]
        try:
            self.collection.insert_one(item)
            # print(item.keys())
        except pymongo.errors.DuplicateKeyError as e:
            pass
        return item