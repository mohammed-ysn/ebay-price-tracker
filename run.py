from file_manager import FileManager
from product import Product
from product_catalogue import ProductCatalogue

if __name__ == '__main__':
    catalogue = ProductCatalogue(Product('174948842042'), Product('313914351201'))
    catalogue.sample_all_products()
