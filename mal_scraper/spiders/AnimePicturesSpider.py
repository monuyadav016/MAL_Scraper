import scrapy
import json
from ..items import AnimePicturesItem
import os
from ..settings import ANIME_ID_FILE, API_URL

class AnimePicturesSpider(scrapy.Spider):
    name = "anime_pictures"

    custom_settings = {
        'ITEM_PIPELINES': {
            'mal_scraper.pipelines.AnimePicturesPipeline': 200
        }
    }

    def start_requests(self):
        if "anime_ids.json" in os.listdir():
            location = ANIME_ID_FILE
        else:
            location = os.path.join("/home/monu/Desktop/Projects/MAL_Scraper/mal_scrapy/mal_scraper", "anime_ids.json")
        with open(location, "r") as id_file:
            anime_objs = json.load(id_file)
        for anime_obj in anime_objs:
            url = "{0}{1}/pictures".format(API_URL, anime_obj["mal_id"])
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AnimePicturesItem()
        if response.status == 200:
            item["json_response"] = json.loads(response.text)
            item["json_response"]["mal_id"] = response.url.split("/")[-2]
            yield item
