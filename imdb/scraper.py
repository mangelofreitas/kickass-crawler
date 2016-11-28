from bs4 import BeautifulSoup
import urllib
import requests



headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "Accept-Encoding": "gzip,deflate",
                "Accept-Language": "pt-PT,pt;,q = 0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2,es;q=0.2",
                "Cache-Control": "no-cache",
                "DNT": "1",
                "Pragma": "no-cache",
                "User-Agent": "Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
            }

title = raw_input('Title of the movie or tv serie: ')

category = 0
while category!='1' and category!='2':
    category = raw_input('Is a movie (1) or a tv show (2): ')
    if category!='1' and category!='2':
        print 'Please choose 1 or 2!'

if category == '1':
    category = 'movies'
else:
    category = 'tv'

f = open('to_download.dat','a')

if category=='tv':
    base_url = 'http://www.imdb.com'
    url = base_url+'/find?ref_=nv_sr_fn&q='+title+'&s=all'
    req = requests.get(url, timeout=10,headers = headers)
    soup = BeautifulSoup(req.content,'html.parser')
    tr = soup.find('tr',class_='findResult odd')
    td = tr.find_all('td')
    new_url = base_url + td[0].find('a')['href']
    new_req = requests.get(new_url,timeout=10,headers = headers)
    new_soup = BeautifulSoup(new_req.content,'html.parser')
    div = new_soup.find('div',class_='seasons-and-year-nav')
    seasons = div.find_all('div')[2].find_all('a')
    episodes_list = list()
    for season in seasons:
        season_url = base_url+season['href']
        season_req = requests.get(season_url,timeout=10,headers=headers)
        season_soup = BeautifulSoup(season_req.content,'html.parser')
        season_div = season_soup.find_all('div',class_='list_item')
        episodes_season = []
        for episode in season_div:
            text = episode.find('div',class_='hover-over-image').find('div').get_text()+', '+episode.find('div',class_='airdate').get_text().strip()
            episodes_season.append(text)
        for item in episodes_list:
            episodes_season.append(item)
        episodes_list = episodes_season
    
    for item in episodes_list:
        f.write(category+' '+title+' '+item+'\n')
else:
     f.write(category+' '+title+'\n')