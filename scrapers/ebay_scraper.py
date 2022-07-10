import requests
from bs4 import BeautifulSoup

from scrapers.abs_scraper import AbsScraper


class EBayScraper(AbsScraper):
    base_url = 'https://www.ebay.co.uk/itm/'

    @staticmethod
    def gen_product_url(prod_id):
        return EBayScraper.base_url + prod_id

    @staticmethod
    def product_code_to_price(prod_code):
        product_url = EBayScraper.gen_product_url(prod_code)
        page = requests.get(product_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        price_element = soup.find('span', {'id': 'prcIsum'})

        if price_element is not None:
            return float(price_element['content'])
        else:
            # price was not found
            return None

    @staticmethod
    def get_price(prod_id):
        product_url = EBayScraper.gen_product_url(prod_id)
        page = requests.get(product_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        prod_panel_element = soup.find('div', {'id': 'LeftSummaryPanel'})

        if prod_panel_element is None:
            return None

        name_element = prod_panel_element.find('span', {'class': 'ux-textspans ux-textspans--BOLD'})

        if name_element is None:
            return None

        return name_element.getText()
