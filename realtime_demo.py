from time import sleep

from product_data.ebay_product import EBayProduct
from product_data.product_catalogue import ProductCatalogue
from visuals.graph import plot_price

if __name__ == "__main__":
    demo_cat = ProductCatalogue(EBayProduct("Gym Bottle", "265163604233"))
    demo_cat.sample_all_prods()
    sleep(1)
    demo_cat.sample_all_prods()
    sleep(1)
    demo_cat.sample_all_prods()
    plot_price(demo_cat.get_prod("265163604233"))
