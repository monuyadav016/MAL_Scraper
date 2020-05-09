A python script to scrap anime details from myanimelist and store it in mongodb database. Requires mongodb for storing the scraped content. This script relies on [Jikan REST API](https://jikan.docs.apiary.io/#) for returning the data as json response.

A backup of database scraped using MAL_Scraper is included in the repository as an archive. To restore it using mongorestore
```
$ mongorestore --gzip --archive=mal_db_2020-05-09.gz --db mal_db
```

The database has following four collections
  - anime_details
  - anime_characters_staff
  - anime_pictures
  - anime_stats

Requirement for any other data apart from this that is not specific to myanimelist was not felt by this project. To install and update the database with new data of upcoming anime read below. Currently the airing anime are not updated with every run and will be fixed in further update.

### Installation
```
$ pip install -r requirements.txt
```

### Run script to create new database
```
$ python start_scraping.py
```

### Run script to update the database
```
$ python parallel_scraper.py
```

The two variables that are of importance are DB_NAME and API_URL in mal_scraper/settings.py. Change them as neccessary based on your database naming. Make sure to change the API_URL if running the local server of Jikan REST API. Tweak other settings once you figure out the structure.

Also read [Bulk Request Jikan API](https://jikan.docs.apiary.io/#introduction/information/bulk-requests)

## Disclaimer
This project does not intend to infringe any of myanimelist's policies. It serves as a web archiver of data of importance to Anime community.
