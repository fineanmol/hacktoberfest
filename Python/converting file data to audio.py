from gtts import gTTS
import os

# Specify the input text file and language
input_file = 'demogen.txt'
language = 'en'

# Read the text from the input file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a gTTS object
output = gTTS(text=text, lang=language, slow=False)

# Specify the output video file
output_file = 'videoout.mp4'

# Save the gTTS output to the video file
output.save(output_file)

# Open the video file using the default video player
os.system(f'start {output_file}')
