from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional


class AbsProduct(ABC):
    def __init__(self, name: str, prod_id: str):
        """Initialise the product.

        Parameters
        ----------
        name : str
            The name of the product.
        prod_id : str
            The ID of the product.

        """
        self.name = name
        self.id = prod_id
        # k: time
        # v: price
        self.price_history: Dict[datetime, float] = {}

    @abstractmethod
    def sample_price(self) -> Optional[float]:
        """Sample the product price.

        Returns
        -------
        Optional[float]
            The sampled price.

        """
        pass

    def most_recent_price(self) -> Optional[float]:
        """Get the most recent sampled price.

        Returns
        -------
        Optional[float]
            The most recent sampled price.

        """
        if len(self.price_history) > 0:
            return self.price_history[max(self.price_history)]
        else:
            return None

    def __str__(self):
        return f"{self.name} @ £{self.most_recent_price()}"
