import scrapy
import json
from ..items import AnimeDetailsItem
import os
from ..settings import ANIME_ID_FILE, API_URL, DB_NAME
from ..helper.helper import get_remaining_id_list

class AnimeDetailsSpider(scrapy.Spider):
    name = "anime_details"
    collection_name = "anime_details"

    custom_settings = {
        'ITEM_PIPELINES': {
            'mal_scraper.pipelines.AnimeDetailsPipeline': 250
        }
    }

    def start_requests(self):
        if "anime_ids.json" in os.listdir():
            location = ANIME_ID_FILE
        else:
            location = os.path.join("/home/monu/Desktop/Projects/MAL_Scraper/mal_scrapy/mal_scraper", "anime_ids.json")
        anime_objs = get_remaining_id_list(DB_NAME, AnimeDetailsSpider.collection_name, location)
        for anime_obj in anime_objs:
            url = "{0}{1}".format(API_URL ,anime_obj["mal_id"])
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AnimeDetailsItem()
        if response.status == 200:
            item["json_response"] = json.loads(response.text)
            yield item
