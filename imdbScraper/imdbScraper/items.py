

from scrapy.item import Item, Field


class ImdbscraperItem(Item):
    season = Field()
    episode = Field()