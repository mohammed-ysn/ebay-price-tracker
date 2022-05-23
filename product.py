from datetime import datetime
from scraper import Scraper


class Product:
    scraper = Scraper()

    def __init__(self, product_code):
        self.product_code = product_code
        self.price_history = {}

    def sample_current_price(self):
        self.price_history[datetime.now()] = self.scraper.product_code_to_price(self.product_code)

    def __str__(self):
        return f'Product object {self.product_code}'
