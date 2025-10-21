'''
HTTP-based Flipkart Product Scraper

This is a lightweight version of the Flipkart scraper that uses simple HTTP requests
instead of browser automation. It requires minimal dependencies and is easier to set up.

First Create a virtual environment and activate it, if not already done: 
python -m venv venv
.\venv\Scripts\activate (on Windows)

INSTALLATION:
pip install -r requirements_http.txt


This version uses simple HTTP requests instead of crawl4ai for better compatibility and lighter dependencies.
It works by sending HTTP requests with proper headers and user-agent rotation to avoid detection.

'''


import os
import sys
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse
import time

class FlipkartScraper:
    def __init__(self, product_url):
        self.product_url = product_url
        self.ua = UserAgent()
        
    def get_headers(self):
        """Get headers with random user agent"""
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
    
    def extract_website_name(self, url):
        """Extract website name from URL"""
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain.split('.')[0].title()

    def extract_flipkart_product(self):
        url = self.product_url
        product_details = {}
        try:
            if sys.platform.startswith('win'):
                sys.stdout.reconfigure(encoding='utf-8')
                print("Running on Windows platform, set encoding to utf-8")

            print("Starting web scraping...")
            
            # Make HTTP request with proper headers
            session = requests.Session()
            session.headers.update(self.get_headers())
            
            print(f"Fetching: {url}")
            response = session.get(url, timeout=10)
            response.raise_for_status()
            
            if response.status_code != 200:
                print(f"Unable to fetch {url}, status code: {response.status_code}")
                return product_details

            print("✓ Successfully fetched page content")
            
            # Add a small delay to be respectful
            time.sleep(1)
            
            soup = BeautifulSoup(response.content, 'html.parser')

            product_details = {}
            product_details["brand"] = self.extract_website_name(url)
            product_details["valid_product_page"] = True
            product_details["physical_product"] = True
            product_details["currency"] = "INR"
            title = soup.find('span', class_='VU-ZEz')
            title_brand = soup.find('span', class_='mEh187')
            if title:
                product_details["title"] = title.get_text(
                    strip=True).replace('\xa0', ' ')
                if title_brand:
                    title_brand = title_brand.get_text(
                        strip=True).replace('\xa0', ' ')
                    product_details['title'] = title_brand + \
                        " "+product_details['title']
            else:
                product_details["title"] = "N/A"
                print(
                    f"Product title not found using .VU-ZEz on {url}: ")
                print(f"Or May be url is not a valid one")
                return product_details

            price = soup.find('div', class_='Nx9bqj CxhGGd yKS4la')
            mrp = soup.find('div', class_='yRaY8j A6+E6v yKS4la')
            discount = soup.select_one('div.UkUFwK.WW8yVX.yKS4la > span')
            if not price:
                price = soup.find('div', class_='Nx9bqj CxhGGd')
                mrp = soup.find('div', class_='yRaY8j A6+E6v')
                discount = soup.select_one('div.UkUFwK.WW8yVX > span')
            if price:
                product_price = price.get_text().strip()[1:]
                product_price = int(product_price.replace(",", ""))
                product_details["price"] = product_price
                if mrp:
                    product_details["mrp"] = int(
                        mrp.get_text().strip()[1:].replace(",", ""))
                else:
                    product_details["mrp"] = "N/A"
                    print(f"Product mrp not found on {url}")
                if discount:
                    product_details["discount"] = discount.get_text().strip()
                else:
                    product_details["discount"] = "N/A"
                    print(f"Product discount not found on {url}")
            else:
                product_details["price"] = "N/A"
                product_details["mrp"] = "N/A"
                product_details["discount"] = "N/A"
                print(f"Product price details not found on {url}")

            buy_now_btn = soup.find(
                "button", class_="QqFHMw vslbG+ _3Yl67G _7Pd1Fp")
            
            # check if product is out of stock for pincode only ?
            check_is_pincode_available=soup.find("div", class_="nyRpc8")
            pincode_out_of_stock_error=False
            if check_is_pincode_available:
                pincode_text = check_is_pincode_available.get_text(strip=True)
                print(f"pincode_text: {pincode_text}")
                if "out of stock" in pincode_text:
                   pincode_out_of_stock_error = True
    
            if buy_now_btn:
                if "disabled" in buy_now_btn.attrs and not pincode_out_of_stock_error:
                    product_details["stock"] = "out_stock"
                    print("❌ Product is out of stock! 'Buy Now' is disabled.")
                else:
                    product_details["stock"] = "in_stock"
                    print("✅ Product is available! 'Buy Now' is enabled.")
            else:
                product_details["stock"] = "out_stock"
                print(
                    "Buy now button not found, means product is not available")

            # stock = soup.find("div", class_="Z8JjpR")
            # if stock:
            #     product_details["stock"] = stock.get_text(strip=True)

            ratings = soup.find('div', class_='XQDdHH')
            reviews = soup.find('span', class_='Wphh3N')

            if ratings:
                product_details["ratings"] = ratings.get_text().strip()
            else:
                product_details["ratings"] = "N/A"
                print(
                    f"Rating start class : XQDdHH not found on {url} ")
            if reviews:
                product_details["reviews"] = reviews.get_text().strip()
                product_details["reviews"] = product_details["reviews"].split(' Ratings')[
                    0].replace(",", "")
            else:
                print(
                    f"Rating count class :Wphh3N not found on {url}")
                product_details["reviews"] = "N/A"

            image = soup.find('img', class_='DByuf4 IZexXJ jLEJ7H')
            if not image:
                image = soup.find('img', class_='_53J4C- utBuJY')

            if image:
                image_url = image['src']
                product_details["image"] = image_url
                print(f"image_url: {image_url}")
                # response = requests.get(image_url)
                # image_name = f"{product_details['title'][:50]}.png"
                # image_name = sanitize_filename(image_name)
                # image_path = os.path.join(os.getcwd(), image_name)
                # with open(image_path, 'wb') as f:
                #     f.write(response.content)
            else:
                print(
                    f"Product image using : .DByuf4 IZexXJ jLEJ7H or ._53J4C- utBuJY not found on {url}")

        # extracting product specs from page
            general_sections = soup.find_all(
                'div', class_='GNDEQ-', string=None)
            target_labels = ["Model Name", "Model",
                             "Item model number", "Style Name", "Model Number"]
            if general_sections:
                for section in general_sections:
                    header = section.find('div', class_='_4BJ2V+')
                    if header:
                        header = header.get_text(strip=True)
                        print(f"header value: {header}")
                        if header == "General":
                            # Filter for the specific section
                            print("header is General")
                            # Locate the table
                            table = section.find('table', class_='_0ZhAN9')
                            if table:
                                rows = table.find_all(
                                    'tr', class_='WJdYP6 row')  # Extract rows
                                if rows:
                                    key_value_pairs = {}
                                    extracted_technical_data = {}
                                    for row in rows:
                                        key_cell = row.find(
                                            'td', class_='+fFi1w col col-3-12')  # Locate key
                                        value_cell = row.find(
                                            'td', class_='Izz52n col col-9-12')  # Locate value

                                        if key_cell and value_cell:
                                            key = key_cell.get_text(strip=True)
                                            value = value_cell.get_text(
                                                strip=True)
                                            key_value_pairs[key] = value
                                            if key in target_labels:
                                                extracted_technical_data[key] = value
                                        else:
                                            print(
                                                f"Product Specifiaction table key and value using .+fFi1w col col-3-12 and .Izz52n col col-9-12 not found on {url} ")

                                    product_details[f"specs"] = key_value_pairs
                                    product_details["technical_details"] = extracted_technical_data
                                    break
                                else:
                                    print(
                                        f"Product General Specifiaction rows using .WJdYP6 row not found on {url}")
                                    product_details["specs"] = "N/A"
                            else:
                                print(
                                    f"Product General Specifications table using ._0ZhAN9 not found in {url}")
                                product_details["specs"] = "N/A"
                        else:
                            print(
                                "General box is not there in header,extractring other details")
                            table = section.find('table', class_='_0ZhAN9')
                            if table:
                                rows = table.find_all(
                                    'tr', class_='WJdYP6 row')  # Extract rows
                                if rows:
                                    key_value_pairs = {}
                                    extracted_technical_data = {}
                                    for row in rows:
                                        key_cell = row.find(
                                            'td', class_='+fFi1w col col-3-12')  # Locate key
                                        value_cell = row.find(
                                            'td', class_='Izz52n col col-9-12')  # Locate value

                                        if key_cell and value_cell:
                                            key = key_cell.get_text(strip=True)
                                            value = value_cell.get_text(
                                                strip=True)
                                            key_value_pairs[key] = value
                                            if key in target_labels:
                                                extracted_technical_data[key] = value
                                    else:
                                        print(
                                            f"Product Specifiaction table key and value using .+fFi1w col col-3-12 and .Izz52n col col-9-12 not found on {url} ")
                                    product_details[f"specs:{header}"] = key_value_pairs
                                    product_details["technical_details"] = extracted_technical_data
                                else:
                                    print(
                                        f"Product  Specifiaction rows using .WJdYP6 row not found on {url}")
                                    # product_details["specs"]="N/A"
                            else:
                                print(
                                    f"Product Specifications table using ._0ZhAN9 not found in {url}")
                                # product_details["specs"]="N/A"
                    else:
                        print(
                            f"Product Sepecification Header using : ._4BJ2V not found on {url}")
                        print(f"Extracting the specification available ")
                        table = section.find('table', class_='_0ZhAN9')
                        if table:
                            rows = table.find_all(
                                'tr', class_='WJdYP6 row') 
                            if rows:
                                key_value_pairs = {}
                                extracted_technical_data = {}
                                for row in rows:
                                    key_cell = row.find(
                                        'td', class_='+fFi1w col col-3-12') 
                                    value_cell = row.find(
                                        'td', class_='Izz52n col col-9-12') 

                                    if key_cell and value_cell:
                                        key = key_cell.get_text(strip=True)
                                        value = value_cell.get_text(strip=True)
                                        key_value_pairs[key] = value
                                        if key in target_labels:
                                            extracted_technical_data[key] = value
                                    else:
                                        print(
                                            f"Product Specifiaction table key and value using .+fFi1w col col-3-12 and .Izz52n col col-9-12 not found on {url} ")
                                product_details[f"specs"] = key_value_pairs
                                product_details["technical_details"] = extracted_technical_data
                            else:
                                print(
                                    f"Product  Specifiaction rows using .WJdYP6 row not found on {url}")
                                product_details["specs"] = "N/A"
                        else:
                            print(
                                f"Product Specifications table using ._0ZhAN9 not found in {url}")
                            product_details["specs"] = "N/A"
            else:
                product_details["specs"] = "N/A"
                print(
                    f"Product Specification general_sections using : GNDEQ- not found on url{url}")
            print(f"Finished crawling for {url}")
            return product_details

        except requests.exceptions.RequestException as e:
            print(f"HTTP request failed: {str(e)} for {url}")
            return product_details
        except Exception as e:
            print(f"An error occurred in scraping: {str(e)} on {url}")
            return product_details

# Example usage
def main():
    # Set the product URL here
    product_url = "https://www.flipkart.com/dell-s-series-68-58-cm-27-inch-full-hd-ips-panel-5-years-warranty-99-srgb-low-blue-light-technology-hdmi-x2-tilt-adjustment-contrast-ratio-1000-1-300-nits-brightness-display-manager-3-sided-bezel-less-monitor-s2721hnm-s2721hn/p/itme14d367b6a471?pid=MONGYDFQE2JJHNF3&lid=LSTMONGYDFQE2JJHNF3HYP52D&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_3&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=b2a0a257-5b21-4771-92f2-5ca744a7a374.MONGYDFQE2JJHNF3.SEARCH&ppt=hp&ppn=homepage&ssid=60ysptb6lc0000001760012340875"
    
    scraper = FlipkartScraper(product_url)
    product_data = scraper.extract_flipkart_product()
    
    print("Product Data:")
    print("-------------")
    for key, value in product_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
