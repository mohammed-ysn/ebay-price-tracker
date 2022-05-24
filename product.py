from datetime import datetime
from scraper import Scraper


class Product:
    scraper = Scraper()

    def __init__(self, product_code):
        self.product_code = product_code
        self.price_history = {}

    def sample_current_price(self):
        sampled_price = self.scraper.product_code_to_price(self.product_code)

        # add newly sampled price to price history
        self.price_history[datetime.now()] = sampled_price

        return sampled_price

    def most_recent_price(self):
        if len(self.price_history) > 0:
            return self.price_history[max(self.price_history, key=self.price_history.get)]
        else:
            return 'n/a'

    def __str__(self):
        return f'Product object {self.product_code} at £{self.most_recent_price()}'
