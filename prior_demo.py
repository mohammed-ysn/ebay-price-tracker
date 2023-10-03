from datetime import datetime
import os

from utils import file_manager
from product.ebay_product import EBayProduct
from product.catalogue import ProductCatalogue

DATA_DIR = os.path.join(".", "data")


def create_demo():
    demo_cat = ProductCatalogue(EBayProduct("Suitcase", "012345"))
    demo_cat.catalogue["012345"].price_history[datetime(2022, 6, 15, 1, 15)] = 56.25
    demo_cat.catalogue["012345"].price_history[datetime(2022, 6, 15, 5, 45)] = 55.5
    demo_cat.catalogue["012345"].price_history[datetime(2022, 6, 15, 12, 13)] = 56.75
    demo_cat.catalogue["012345"].price_history[datetime(2022, 6, 15, 18, 23)] = 55
    demo_cat.catalogue["012345"].price_history[datetime(2022, 6, 15, 22, 6)] = 55

    file_manager.dump(os.path.join(DATA_DIR, "demo_catalogue"), demo_cat)
    print(f"Created {os.path.join(DATA_DIR, 'demo_catalogue')}")


if __name__ == "__main__":
    create_demo()

    catalogue = file_manager.load(os.path.join(DATA_DIR, "demo_catalogue"))
    product = catalogue.get("012345")
    product.plot_price()
