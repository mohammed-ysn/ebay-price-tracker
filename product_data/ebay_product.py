from datetime import datetime
from typing import Optional
from warnings import warn

from product_data.abs_product import AbsProduct
from scrapers.ebay_scraper import EBayScraper


class EBayProduct(AbsProduct):
    def sample_price(self) -> Optional[float]:
        """Sample the product price.

        Returns
        -------
        Optional[float]
            The sampled price.
        """
        sampled_price = EBayScraper.scrape_price(self.id)

        if sampled_price is not None:
            # add newly sampled price to price history
            self.price_history[datetime.now()] = sampled_price
            print(f"Sampled {self.name} @ {sampled_price}")
        else:
            warn(f"Failed to sample price for: {self.id}")

        return sampled_price
