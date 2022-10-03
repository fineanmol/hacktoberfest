import webbrowser
import time
from pykeyboard import PyKeyboard
#hactoberfest2022
count = 0
# replace your target website in the urls
urls = ['www.google.com','www.leetcode.com','www.github.com']
k = PyKeyboard()

# use the count to open the website to any number of times you want
while count != 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(5)
        # for Windows change Command to control to close browser tab after 5 sec
        k.press_keys(['Command','W'])
        count = count + 1 
    
else:
    pass
