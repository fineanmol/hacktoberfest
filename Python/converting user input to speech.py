from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox  # For displaying messages

# Initialize the Tkinter root window
root = Tk()
root.title("Text to Speech Converter")  # Set a title for the window

# Create a canvas to hold the entry and button
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def texttospeech():
    text = entry.get().strip()  # Get text and remove leading/trailing spaces
    if not text:  # Check if the entry is empty
        messagebox.showwarning("Input Error", "Please enter some text!")  # Show warning
        return
    
    output = gTTS(text=text, lang='en', slow=False)
    output_file = 'output.mp3'  # Changed to .mp3 for better compatibility
    output.save(output_file)
    
    # Play the audio file
    os.system(f'start {output_file}')  # Use f-string for better readability

# Create an Entry widget for user input
entry = Entry(root, width=40)  # Set a width for the entry
canvas.create_window(200, 180, window=entry)

# Create a Button widget to trigger the text-to-speech conversion
button = Button(root, text="Start", command=texttospeech)
canvas.create_window(200, 230, window=button)

# Run the Tkinter event loop
root.mainloop()
