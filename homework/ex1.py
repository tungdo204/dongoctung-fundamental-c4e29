from urllib.request import urlopen
from bs4 import BeautifulSoup
from pyexcel import *
from pyexcel_xls import *
from pyexcel_xlsx import *
from collections import OrderedDict
from youtube_dl import YoutubeDL
#1. Open Connection
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')

#2. Find ROI (Region of Interest)
soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find("section","section chart-grid")
div = section.div
ul = div.ul
li_list = ul.find_all("li")

song_list = []
for li in li_list:
    h3 = li.h3
    a = h3.a
    h4 = li.h4
    a_2 = h4.a
    title = a.string.strip()
    artist = a_2.string.strip()
    song = OrderedDict({
        'Title': title,
        'Artist' : artist
    })
    song_list.append(song)
# save_as(records=song_list, dest_file_name="itunes.xls")
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (audio)
    
}

for i in range(len(song_list)):
    ytsearch = song_list[i]['Title'] + ' ' + song_list[i]['Artist']
    YoutubeDL(options).download([ytsearch])

 


