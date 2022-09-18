from abc import ABC, abstractmethod
from typing import Optional


class AbsScraper(ABC):
    @staticmethod
    @abstractmethod
    def scrape_price(prod_id: str) -> Optional[float]:
        """Scrape the price of a product from the website.

        Parameters
        ----------
        prod_id : str
            The product ID.

        Returns
        -------
        Optional[float]
            The product price.

        """
        pass
