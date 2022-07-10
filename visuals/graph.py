import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'consolas'


def plot_price(prod):
    # create a figure containing a single axes
    fig, ax = plt.subplots()

    # convert keys to datetime array in minutes
    timestamps = np.fromiter(prod.price_history.keys(), dtype='datetime64[m]')
    # convert prices to float array
    prices = np.fromiter(prod.price_history.values(), dtype='float')
    ordering = timestamps.argsort()

    # plot max and min prices only if they are different
    if len(prices) > 0:
        min_price = np.min(prices)
        max_price = np.max(prices)
        if min_price != max_price:
            # plot max and min horizontal lines
            ax.axhline(y=min_price, color='green', linestyle='dashed', alpha=0.7)
            ax.axhline(y=max_price, color='red', linestyle='dashed', alpha=0.7)
            ax.text(timestamps[ordering[0]], min_price, f'£{min_price:.2f}')
            ax.text(timestamps[ordering[0]], max_price, f'£{max_price:.2f}')

    # plot price step graph
    ax.step(timestamps[ordering], prices[ordering], where='post')

    ax.set_xlabel('Time')
    ax.set_ylabel('Price')

    ax.yaxis.set_major_formatter('£{x:1.2f}')

    ax.grid(alpha=0.3)

    fig.canvas.manager.set_window_title(f'{prod.name} Price History')
    fig.suptitle(f'{prod.name} Price History')

    plt.xticks(rotation=17)

    plt.show()
