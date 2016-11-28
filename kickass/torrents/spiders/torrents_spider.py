from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from kickass.items import KickassItem


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TorrentsSpider(Spider):
    name = "torrents"
    allowed_domains = ["thepiratebay.org"]
    #trabalhar com o thepiratebay.org

    def __init__(self, *args, **kwargs):
        super(KickassSpider, self).__init__(*args, **kwargs)
        self.keywords = kwargs['keywords']
        self.category = kwargs['category']
        if self.category == 'movies':
            self.start_urls = [
                'https://thepiratebay.org/search/'
                + self.keywords
                + '/0/99/201/'
            ]
        else:
            self.start_urls = [
                'https://thepiratebay.org/search/'
                + self.keywords
                + '/0/99/205/'
            ]
        
        print self.start_urls

    def parse(self, response):
        next = 0
        selector = Selector(response)
        entries = selector.xpath('//tr[starts-with(@id,"torrent_")]')
        items = []
        n = 0
        print "\n			<<<<<< TORRENTS >>>>>>\n"
        for entry in entries:
			n = n+1
			item = TorrentsItem()
			item['title'] = entry.select('td[1]/div[2]/div[1]/a[1]/node()').extract()
			item['title'] = ''.join(item['title'])
			item['title'] = re.sub("<.*?>","",item['title'])
			item['url'] = entry.select('td[1]/div[2]/a[2]/@href').extract()
			item['url'] = ''.join(item['url'])
			item['torrent'] = entry.select('td[1]/div[1]/a[starts-with(@title,"Download torrent file")]/@href').extract()
			item['torrent'] = ''.join(item['torrent'])
			item['size'] = entry.select('td[2]/text()[1]').extract()
			item['size'] = ''.join(item['size'])
			item['sizeType'] = entry.select('td[2]/span/text()').extract()
			item['sizeType'] = ''.join(item['sizeType'])
			item['age'] = entry.select('td[4]/text()').extract()
			item['age'] = ''.join(item['age'])
			item['seed'] = entry.select('td[5]/text()').extract()
			item['seed'] = ''.join(item['seed'])
			item['leech'] = entry.select('td[6]/text()').extract()
			item['leech'] = ''.join(item['leech'])
			items.append(item)
			print str(n) +' Title -> '+item['title'] +"		-> Size: " + str(item['size']) + " " + item['sizeType'] + bcolors.OKGREEN + "		-> Seed: " + str(item['seed']) + bcolors.FAIL + "		-> Leech: " + str(item['leech']) + bcolors.ENDC
        next = int(raw_input('Which Torrent to Download? 1/'+str(n)+'\n -> '))
        if(next <= 0) or (next >n):
            return None
        return items[next-1]
    
