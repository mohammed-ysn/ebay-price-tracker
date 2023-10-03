from typing import Optional
import requests
from bs4 import BeautifulSoup

from scraper.scraper import Scraper


class EBayScraper(Scraper):
    base_url = "https://www.ebay.co.uk/itm/"

    @staticmethod
    def get_product_url(prod_id: str) -> str:
        """Get a product page URL."""
        return EBayScraper.base_url + prod_id

    @staticmethod
    def scrape_price(prod_id: str) -> Optional[float]:
        """Scrape the price of a product from the website."""
        product_url = EBayScraper.get_product_url(prod_id)
        page = requests.get(product_url)
        soup = BeautifulSoup(page.text, "html.parser")
        price_element = soup.find("span", {"id": "prcIsum"})

        if price_element is not None:
            return float(price_element["content"])
        else:
            # price was not found
            return None
