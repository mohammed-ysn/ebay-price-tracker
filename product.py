from datetime import datetime
from ebay_scraper import EBayScraper


class Product:
    def __init__(self, prod_code):
        self.code = prod_code
        self.name = ''
        self.update_name()
        self.price_history = {}

    def sample_current_price(self):
        sampled_price = EBayScraper.product_code_to_price(self.code)

        if sampled_price is not None:
            # add newly sampled price to price history
            self.price_history[datetime.now()] = sampled_price
        else:
            print(f'Failed to sample price for: {self.code}')

        return sampled_price

    def most_recent_price(self):
        if len(self.price_history) > 0:
            return self.price_history[max(self.price_history, key=self.price_history.get)]
        else:
            return '[PRICE NOT FOUND]'

    def update_name(self):
        name_found = EBayScraper.product_code_to_name(self.code)
        if name_found is not None:
            self.name = name_found
        else:
            print(f'Failed to update name for: {self.code}')

    def get_name(self):
        return self.name if self.name is not None else '[NAME NOT FOUND]'

    def get_link(self):
        return f'{EBayScraper.base_url}{self.code}'

    def __str__(self):
        return f'{self.code} {self.get_name()} @ £{self.most_recent_price()}'
