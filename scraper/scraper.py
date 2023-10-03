from abc import ABC, abstractmethod
from typing import Optional


class Scraper(ABC):
    @staticmethod
    @abstractmethod
    def scrape_price(prod_id: str) -> Optional[float]:
        """Scrape the price of a product."""
        pass
