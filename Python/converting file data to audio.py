from gtts import gTTS
import os

input_file = 'demogen.txt'
language = 'en'
output_file = 'videoout.mp4'

try:
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    output = gTTS(text=text, lang=language, slow=False)
    output.save(output_file)
    os.system(f'start {output_file}')
except Exception as e:
    print(f"An error occurred: {e}")