from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional
import matplotlib.pyplot as plt
import numpy as np


class Product(ABC):
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

    def plot_price(self) -> None:
        timestamps = np.fromiter(self.price_history.keys(), dtype="datetime64[s]")
        prices = np.fromiter(self.price_history.values(), dtype="float")

        # Sort data by timestamps
        sorted_indices = np.argsort(timestamps)
        timestamps = timestamps[sorted_indices]
        prices = prices[sorted_indices]

        fig, ax = plt.subplots()

        # Plot max and min prices if they are different
        min_price = np.min(prices)
        max_price = np.max(prices)
        if min_price != max_price:
            ax.axhline(y=min_price, color="green", linestyle="dashed", alpha=0.7)
            ax.axhline(y=max_price, color="red", linestyle="dashed", alpha=0.7)
            ax.text(timestamps[0], min_price, f"£{min_price:.2f}")
            ax.text(timestamps[0], max_price, f"£{max_price:.2f}")

        # Plot price step graph
        ax.step(timestamps, prices, where="post")

        ax.scatter(timestamps, prices, marker="x", color="black", alpha=0.7)

        ax.set_xlabel("Time")
        ax.set_ylabel("Price")

        # Use currency formatting for y-axis
        ax.yaxis.set_major_formatter("£{x:1.2f}")

        ax.grid(alpha=0.3)

        fig.canvas.manager.set_window_title(f"{self.name} Price History")
        fig.suptitle(f"{self.name} Price History")

        # Rotate x-axis labels for readability
        plt.xticks(rotation=17)

        plt.show()

    def __str__(self):
        return f"{self.name} @ £{self.most_recent_price()}"
