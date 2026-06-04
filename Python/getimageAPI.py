import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, send_file

app = Flask(__name)

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_first_image(search_html):
    soup = BeautifulSoup(search_html, 'html.parser')
    img_div = soup.find("div", {"class": "rg_i"})
    if img_div:
        img_url = img_div.find("img")["src"]
        return img_url
    else:
        return None

@app.route('/get_first_image', methods=['GET'])
def get_first_image():
    query = request.args.get('query')
    search_html = google_search(query)

    if search_html:
        img_url = extract_first_image(search_html)
        if img_url:
            return jsonify({'image_url': img_url})
        else:
            return jsonify({'error': 'No image found in the search results.'})
    else:
        return jsonify({'error': 'Failed to retrieve search results.'})

if __name__ == "__main__":
    app.run(debug=True)
# http://localhost:5000/get_first_image?query=hacktoberfest2023
