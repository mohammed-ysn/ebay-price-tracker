from unittest import TestCase

import numpy as np

from product import Product
from visuals.graph import graph_prices


class Test(TestCase):
    def test_graph_prices(self):
        p = Product('265163604233')
        p.price_history = {
            np.datetime64('2005-02-25'): 5.02,
            np.datetime64('2005-07-29'): 5.66,
            np.datetime64('2006-01-14'): 4.27
        }
        graph_prices(p)
