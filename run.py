from product import Product
from product_catalogue import ProductCatalogue
from visuals.graph import graph_prices

if __name__ == '__main__':
    catalogue = ProductCatalogue(Product('174948842042'), Product('265163604233'))
    p = catalogue.get_prod('174948842042')
    p.sample_current_price()
    p.sample_current_price()
    p.sample_current_price()
    graph_prices(p)
