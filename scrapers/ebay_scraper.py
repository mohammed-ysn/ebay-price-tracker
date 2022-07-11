import requests
from bs4 import BeautifulSoup

from scrapers.abs_scraper import AbsScraper


class EBayScraper(AbsScraper):
    base_url = 'https://www.ebay.co.uk/itm/'

    @staticmethod
    def gen_product_url(prod_id):
        return EBayScraper.base_url + prod_id

    @staticmethod
    def scrape_price(prod_code):
        product_url = EBayScraper.gen_product_url(prod_code)
        page = requests.get(product_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        price_element = soup.find('span', {'id': 'prcIsum'})

        if price_element is not None:
            return float(price_element['content'])
        else:
            # price was not found
            return None
