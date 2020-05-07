import scrapy
import json
from ..items import AnimeCharactersStaffItem
import os
from ..settings import ANIME_ID_FILE, API_URL, DB_NAME
from ..helper.helper import get_remaining_id_list

class AnimeCharactersStaffSpider(scrapy.Spider):
    name = "anime_characters_staff"
    collection_name = "anime_characters_staff"

    custom_settings = {
        'ITEM_PIPELINES': {
            'mal_scraper.pipelines.AnimeCharactersStaffPipeline': 200
        }
    }

    def start_requests(self):
        if "anime_ids.json" in os.listdir():
            location = ANIME_ID_FILE
        else:
            location = os.path.join("/home/monu/Desktop/Projects/MAL_Scraper/mal_scrapy/mal_scraper", "anime_ids.json")
        anime_objs = get_remaining_id_list(DB_NAME, AnimeCharactersStaffSpider.collection_name, location)
        for anime_obj in anime_objs:
            url = "{0}{1}/characters_staff".format(API_URL, anime_obj["mal_id"])
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AnimeCharactersStaffItem()
        if response.status == 200:
            item["json_response"] = json.loads(response.text)
            item["json_response"]["mal_id"] = int(response.url.split("/")[-2])
            yield item