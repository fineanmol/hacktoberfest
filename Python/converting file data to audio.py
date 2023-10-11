from gtts import gTTS
import os
import subprocess

try:
    text = open('demogen.txt', 'r', encoding='utf-8').read()
    language = 'en'
    
    # Specify the output file format (audio)
    output = gTTS(text=text, lang=language, slow=False)
    output.save('audioout.mp3')
    
    print("Text converted to audio successfully!")

    # Use subprocess to open the audio file
    subprocess.Popen(['start', 'audioout.mp3'], shell=True)
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
