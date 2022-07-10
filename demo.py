from datetime import datetime

from ebay_product import EBayProduct
import file_manager
from product_catalogue import ProductCatalogue
from visuals.graph import plot_price


def create_demo():
    cat = ProductCatalogue(EBayProduct('Suitcase', '012345'))
    cat.catalogue['012345'].price_history[datetime(2022, 6, 15, 1, 15)] = 56.25
    cat.catalogue['012345'].price_history[datetime(2022, 6, 15, 5, 45)] = 55.5
    cat.catalogue['012345'].price_history[datetime(2022, 6, 15, 12, 13)] = 56.75
    cat.catalogue['012345'].price_history[datetime(2022, 6, 15, 18, 23)] = 55
    cat.catalogue['012345'].price_history[datetime(2022, 6, 15, 22, 6)] = 55
    file_manager.dump('demo_catalogue.pkl', cat)
    print('Created demo_catalogue.pkl')


if __name__ == '__main__':
    cat = file_manager.load('demo_catalogue.pkl')
    plot_price(cat.get_prod('012345'))
