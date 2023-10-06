from gtts import gTTS
import os

text=open('demogen.txt','r',encoding='utf-8').read()
language='en'
output=gTTS(text=text,lang=language,slow=False)
output.save('videoout.mp4')
os.system('start videoout.mp4')