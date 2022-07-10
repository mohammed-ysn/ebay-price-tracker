from ebay_product import EBayProduct
from product_catalogue import ProductCatalogue
from visuals.graph import plot_price

if __name__ == '__main__':
    catalogue = ProductCatalogue(EBayProduct('Ball Point Pen Biros', '174948842042'), EBayProduct('hello', 'fakeid'))
    catalogue.sample_all_prods()
    print(catalogue)
    for prod in catalogue.get_all_prods():
        print(prod.get_link())
