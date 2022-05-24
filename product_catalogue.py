class ProductCatalogue:
    def __init__(self, *products):
        # dict product code -> product obj
        self.catalogue = {}
        for product in products:
            self.catalogue[product.product_code] = product

    def sample_all_products(self):
        for prod in self.catalogue.values():
            prod.sample_current_price()

    def __str__(self):
        msg = ""
        for prod in self.catalogue.values():
            msg += str(prod) + "\n"
        return msg