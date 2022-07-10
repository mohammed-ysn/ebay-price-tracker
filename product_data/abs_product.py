from abc import ABC, abstractmethod


class AbsProduct(ABC):
    def __init__(self, name, prod_id):
        self.name = name
        self.id = prod_id
        self.price_history = {}

    @abstractmethod
    def sample_price(self):
        pass

    def most_recent_price(self):
        if len(self.price_history) > 0:
            return self.price_history[max(self.price_history, key=self.price_history.get)]
        else:
            return '[PRICE NOT FOUND]'

    @abstractmethod
    def get_link(self):
        pass

    def __str__(self):
        return f'{self.name} @ £{self.most_recent_price()}'
