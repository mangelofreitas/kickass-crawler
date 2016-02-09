from scrapy import Spider

class ImdbSpider(Spider):
	name = "imdbspider"
	allowed_domains = ["imdb.com"]
	start_urls = ["http://www.imdb.com/"]

def parse(self, response):
	selector = Selector(response)
	entries = selector.xpath('//input[starts-with(@id,"navbar-query")]')
	for entry in entries:
		