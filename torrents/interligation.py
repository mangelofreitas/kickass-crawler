import subprocess
import re

file = open("to_download.dat",'r+')
for line in file:
    dictionary = eval(line)
    category = dictionary['category']
    split = dictionary['item'].split(', ')
    season = re.sub('S','',split[0])
    episode = re.sub('Ep','',split[1])
    if int(season) < 10:
        season = '0'+season
    if int(episode) < 10:
        episode = '0'+episode
    keywords = dictionary['title']+' S'+season+'E'+episode
    print 'Crawling '+keywords
    process = subprocess.Popen('scrapy crawl torrents -a keywords="'+keywords+'" -a category="'+category+'"', stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0]
    print output