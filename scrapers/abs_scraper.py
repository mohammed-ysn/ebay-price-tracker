from abc import ABC, abstractmethod


class AbsScraper(ABC):
    @property
    @abstractmethod
    def base_url(self):
        pass

    @staticmethod
    @abstractmethod
    def scrape_price(prod_id):
        pass
