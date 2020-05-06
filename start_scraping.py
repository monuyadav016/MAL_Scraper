from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from mal_scraper.spiders.AnimeIdSpider import AnimeIdSpider
from mal_scraper.spiders.AnimeDetailsSpider import AnimeDetailsSpider
from mal_scraper.spiders.AnimeCharaterStaffSpider import AnimeCharactersStaffSpider
from mal_scraper.spiders.AnimeStatsSpider import AnimeStatsSpider
from mal_scraper.spiders.AnimePicturesSpider import AnimePicturesSpider

if __name__ == '__main__':

    configure_logging()
    runner = CrawlerRunner(settings=get_project_settings())
    
    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(AnimeIdSpider)
        yield runner.crawl(AnimeDetailsSpider)
        yield runner.crawl(AnimeCharactersStaffSpider)
        yield runner.crawl(AnimeStatsSpider)
        yield runner.crawl(AnimePicturesSpider)
        reactor.stop()

    crawl()
    reactor.run() # the script will block here until the last crawl call is finished