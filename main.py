import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.co.uk/itm/165377260068"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
price = soup.find("span", {"itemprop": "price"}).get("content")
print(price)
