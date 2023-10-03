import matplotlib.pyplot as plt
import numpy as np

from product.product import Product


def plot_price(prod: Product) -> None:
    """Plot product price history.

    Parameters
    ----------
    prod : AbsProduct
        The product to plot.

    """
    timestamps = np.fromiter(prod.price_history.keys(), dtype="datetime64[s]")
    prices = np.fromiter(prod.price_history.values(), dtype="float")

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

    ax.set_xlabel("Time")
    ax.set_ylabel("Price")

    # Use currency formatting for y-axis
    ax.yaxis.set_major_formatter("£{x:1.2f}")

    ax.grid(alpha=0.3)

    fig.canvas.manager.set_window_title(f"{prod.name} Price History")
    fig.suptitle(f"{prod.name} Price History")

    # Rotate x-axis labels for readability
    plt.xticks(rotation=17)

    plt.show()
