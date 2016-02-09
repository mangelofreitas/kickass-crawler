#!/bin/bash
# Downloads .torrent files from kickass.com links
# following redirects and getting the actual torrent
# filename, then runs transmission torrent client
AGENT="'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4)'"
#name=`echo $1 | sed 's/.*kat.ph.//'`".torrent"
#url=`echo $1 | cut -c3-`
#echo $name='torrents/kickass.torrent.tmp'
curl --globoff --compressed -A '$AGENT' -L --post302 $1 > 'torrents/kickass.torrent'
roxterm -e rtorrent 'torrents/kickass.torrent'