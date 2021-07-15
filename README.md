# metallum_scrape
A simple scraper for https://www.metal-archives.com/ using scrapy. Some small improvements can be made to this that I might get around to, but for now just load up req.txt and it will scrape basic information from the site and store it in a csv/json.

## Usage: In terminal
scrapy crawl metallum -O file.csv (or file.json)

## TODO
* scrape each band page individually for more information
* clean req.txt
* currently only supports single requests
