from time import sleep

from product.ebay_product import EBayProduct
from product.catalogue import ProductCatalogue

if __name__ == "__main__":
    product = EBayProduct("Demo Product", input("Enter product ID: "))
    catalogue = ProductCatalogue(product)
    print("Sampling product price...")
    catalogue.sample_all_prods()
    sleep(1)
    print("Sampling product price again...")
    catalogue.sample_all_prods()
    sleep(1)
    print("Sampling product price one last time...")
    catalogue.sample_all_prods()
    product.plot_price()
