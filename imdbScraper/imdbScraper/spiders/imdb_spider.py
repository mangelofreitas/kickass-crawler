from scrapy.spiders import Spider
from scrapy.selector import Selector
from imdbScraper.items import ImdbscraperItem

class ImdbSpider(Spider):
	name = "imdbspider"
	allowed_domains = ["imdb.com"]

	def __init__(self, *args, **kwargs):
		super(ImdbSpider,self).__init__(*args, **kwargs)
		self.start_urls = ['http://www.imdb.com/']
		print self.start_urls

	def parse(self, response):
		selector = Selector(response)
		entries = selector.xpath('//input[starts-with(@id,"navbar-query")]')
		
