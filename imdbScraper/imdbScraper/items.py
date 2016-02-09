

import scrapy


class ImdbscraperItem(scrapy.Item):
    season = scrapy.Item()
    episode = scrapy.Item()