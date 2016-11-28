from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from torrents.items import TorrentsItem


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
        super(TorrentsSpider, self).__init__(*args, **kwargs)
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
        entries = selector.xpath('//tr[not(@class="header")]')
        items = []
        n = 0
        for entry in entries:
            item = TorrentsItem()
            item['title'] = entry.select('td[2]/div[1]/a[1]/text()').extract()
            item['title'] = ''.join(item['title'])
            item['url'] = entry.select('td[2]/div[1]/a[1]/@href').extract()
            item['url'] = ''.join(item['url'])
            item['torrent'] = entry.select('td[2]/a[starts-with(@title,"Download this torrent")]/@href').extract()
            item['torrent'] = ''.join(item['torrent'])
            item['seed'] = entry.select('td[3]/text()').extract()
            item['seed'] = ''.join(item['seed'])
            item['leech'] = entry.select('td[4]/text()').extract()
            item['leech'] = ''.join(item['leech'])
            return item
        file = open('not_found.pbay','a')
        file.write(str(self.keywords)+" <-> "+str(self.start_urls)+"\n")
        file.close()
        return None
        # print "\n			<<<<<< TORRENTS >>>>>>\n"
        # for entry in entries:
		# 	n = n+1
		# 	item = TorrentsItem()
		# 	item['title'] = entry.select('td[2]/div[1]/a[1]/text()').extract()
		# 	item['title'] = ''.join(item['title'])
		# 	item['url'] = entry.select('td[2]/div[1]/a[1]/@href').extract()
		# 	item['url'] = ''.join(item['url'])
		# 	item['torrent'] = entry.select('td[2]/a[starts-with(@title,"Download this torrent")]/@href').extract()
		# 	item['torrent'] = ''.join(item['torrent'])
		# 	item['seed'] = entry.select('td[3]/text()').extract()
		# 	item['seed'] = ''.join(item['seed'])
		# 	item['leech'] = entry.select('td[4]/text()').extract()
		# 	item['leech'] = ''.join(item['leech'])
		# 	items.append(item)
		# 	print str(n) +' Title -> '+item['title'] + bcolors.OKGREEN + "		-> Seed: " + str(item['seed']) + bcolors.FAIL + "		-> Leech: " + str(item['leech']) + bcolors.ENDC
        # next = int(raw_input('Which Torrent to Download? 1/'+str(n)+'\n -> '))
        # if(next <= 0) or (next >n):
        #     return None
        # return items[next-1]
    
