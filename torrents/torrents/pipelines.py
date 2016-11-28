# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import subprocess
import time
import os

class TorrentsPipeline(object):

    def __init__(self):
        if not os.path.exists('torrents'):
            os.makedirs('torrents')

    def process_item(self, item, spider):
        if item!=None:
            if not self.exists(item['title']):
                self.download_item(item)
                time.sleep(5) # pause to prevent 502 eror and hammering
        return item

    def download_item(self, item):
        if item!=None:
            title = item['title']
            f = open('torrents/torrents.log', 'a')
            f.write(title + "\n")
            f.close()
            #print item['torrent']
            path = item['torrent']
            #path = path[2:]
            #print 'Path 2: '+path
            print 'Adding ' + title
            file = open('to_download.pbay', 'a')
            file.write(path+'\n')
            #process = subprocess.Popen("bash\nsh curl_torrent.sh "+path,stdout=subprocess.PIPE,shell=True)
            #output = process.communicate()[0]
            #print output
        else:
            print "No torrent found"

    def exists(self, title):
        for line in open('torrents/torrents.log','a+'):
            if title in line:
                print 'exists -> True'
                return True
        print 'exists -> False'
        return False