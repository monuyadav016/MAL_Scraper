import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mal_scraper.spiders.AnimeDetailsSpider import AnimeDetailsSpider
from mal_scraper.spiders.AnimeCharaterStaffSpider import AnimeCharactersStaffSpider
from mal_scraper.spiders.AnimeStatsSpider import AnimeStatsSpider
from mal_scraper.spiders.AnimePicturesSpider import AnimePicturesSpider


def main():
	process = CrawlerProcess(settings=get_project_settings())
	# process.crawl(AnimeDetailsSpider)
	process.crawl(AnimeCharactersStaffSpider)
	process.crawl(AnimeStatsSpider)
	process.crawl(AnimePicturesSpider)
	process.start() # the script will block here until all crawling jobs are finished

if __name__ == '__main__':
	main()