import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'consolas'


def graph_prices(prod):
    # create a figure containing a single axes
    fig, ax = plt.subplots()

    # plot each product's price history
    price_history = prod.get_price_history()
    timestamps = price_history.keys()
    prices = price_history.values()
    name = prod.get_name()

    # plot max and min prices
    if prices:
        min_price = min(prices)
        max_price = max(prices)
        if min_price != max_price:
            ax.axhline(y=min_price, color='green', linestyle='dashed', alpha=0.7)
            ax.axhline(y=max_price, color='red', linestyle='dashed', alpha=0.7)
            ax.text(min(timestamps), min_price, f'£{min_price}')
            ax.text(min(timestamps), max_price, f'£{max_price}')


    # plot price step graph
    ax.step(timestamps, prices, where='post', label=name)

    ax.set_xlabel('Time')
    ax.set_ylabel('Price')

    ax.yaxis.set_major_formatter('£{x:1.2f}')
    ax.grid(alpha=0.3)

    fig.suptitle('Price History')

    plt.xticks(rotation=17)
    plt.show()


def remove_unchanged_prices(timestamps, prices):
    print(timestamps)
    print(prices)
