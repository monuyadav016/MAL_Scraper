import scrapy
from ..items import AnimeIdItem

class AnimeIdSpider(scrapy.Spider):
    name = "anime_id"

    custom_settings = {
        "FEEDS": {
            "anime_ids.json": {"format": "json"},
        }
    }

    def start_requests(self):
        urls = [
        "https://myanimelist.net/topanime.php"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        item = AnimeIdItem()
        anime_urls = response.css(".hoverinfo_trigger.fl-l.ml12.mr8::attr(href)").getall()
        for anime_url in anime_urls:
            item["mal_id"] = int(anime_url.split("/")[-2])
            yield item

        next_page = response.css(".next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)