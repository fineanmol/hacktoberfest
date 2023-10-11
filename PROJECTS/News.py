import pyttsx3
import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json


def fetch_news(event=None):
    text = entry.get()
    if not text:
        messagebox.showinfo("Input Error", "Please enter a search term.")
        return

    url = f"https://newsapi.org/v2/everything?q={text}&from=2023-07-13&sortBy=publishedAt&apiKey=e4194767f3ad4d28ac9dadfabc640932"
    response = requests.get(url)
    news_data = response.json()

    news_text.delete(1.0, tk.END)
    for article in news_data.get("articles", []):
        title = article.get("title", "No Title")
        description = article.get("description", "No Description")
        news_text.insert(tk.END, f"Title: {title}\n", "title")
        news_text.insert(tk.END, f"Description: {description}\n", "description")
        news_text.insert(tk.END, "-" * 70 + "\n", "separator")
        news_text.insert(tk.END, "\n" * 2)


def read_news_aloud():
    news_content = news_text.get(1.0, tk.END)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can change the voice index
    engine.say(news_content)
    engine.runAndWait()


# Create the main window
root = tk.Tk()
root.title("News App")

# Create and place widgets
label = tk.Label(root, text="Enter your news interest:", font=("Helvetica", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 12), width=50)
entry.pack()

fetch_button = tk.Button(root, text="Fetch News", font=("Helvetica", 12), command=fetch_news)
fetch_button.pack(pady=10)

news_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=60, font=("Helvetica", 12))
news_text.pack(padx=10, pady=5)  # Add x-axis (horizontal) margin using padx

read_aloud_button = tk.Button(root, text="Read News Aloud", font=("Helvetica", 12), command=read_news_aloud)
read_aloud_button.pack(pady=10)

# Configure tag styles
news_text.tag_configure("title", font=("Helvetica", 14, "bold"))
news_text.tag_configure("description", font=("Helvetica", 12), spacing1=8)
news_text.tag_configure("separator", font=("Helvetica", 8), foreground="gray")

# Bind Enter key press event to fetch_news function
entry.bind("<Return>", fetch_news)

root.mainloop()
