from datetime import datetime

from product_data.abs_product import AbsProduct
from scrapers.ebay_scraper import EBayScraper


class EBayProduct(AbsProduct):
    def sample_price(self):
        sampled_price = EBayScraper.scrape_price(self.id)

        if sampled_price is not None:
            # add newly sampled price to price history
            self.price_history[datetime.now()] = sampled_price
            print(f'Sampled {self.name} @ {sampled_price}')
        else:
            print(f'[WARNING] Failed to sample price for: {self.id}')

        return sampled_price
