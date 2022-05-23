import requests
from bs4 import BeautifulSoup


class Scraper:
    base_url = 'https://www.ebay.co.uk/itm/'

    def get_product_url(self, product_code):
        return self.base_url + product_code

    def product_code_to_price(self, product_code):
        product_url = self.get_product_url(product_code)
        page = requests.get(product_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return float(soup.find('span', {'id': 'prcIsum'})['content'])
