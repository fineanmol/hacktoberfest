import urllib.request
import re

query = "moves like jaggers"

def search_yt(a):
    a = a.replace(' ','+')
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+a)
    decoded = html.read().decode()
    video_ids = re.findall("watch\?v=(\S{11})", decoded)
    return video_ids
    
video_ids = search_yt(query)
for id in video_ids:
        print('https://www.youtube.com/watch?v='+id)
