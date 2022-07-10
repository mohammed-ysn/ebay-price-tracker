from unittest import TestCase
import numpy as np

from product_data.ebay_product import EBayProduct
from visuals.graph import plot_price


class Test(TestCase):
    def test_graph_prices(self):
        p = EBayProduct('A very real product', '265163604233')
        p.price_history = {
            np.datetime64('2005-02-25'): 5.02,
            np.datetime64('2005-07-29'): 5.66,
            np.datetime64('2006-01-14'): 4.27,
            np.datetime64('2006-03-02'): 4.27
        }
        plot_price(p)
