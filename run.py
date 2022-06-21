from product import Product
from product_catalogue import ProductCatalogue

if __name__ == '__main__':
    catalogue = ProductCatalogue(Product('174948842042'), Product('265163604233'), Product('hello'))
    catalogue.sample_all_prods()
    print(catalogue)
    for prod in catalogue.get_all_prods():
        print(prod.get_link())
