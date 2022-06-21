class ProductCatalogue:
    def __init__(self, *prods):
        # dict product code -> product obj
        self.catalogue = {}
        for prod in prods:
            self.catalogue[prod.code] = prod

    def sample_all_prods(self):
        for prod in self.catalogue.values():
            prod.sample_current_price()

    def sample_prod(self, prod_code):
        self.catalogue[prod_code].sample_current_price()

    def remove_prod(self, prod_code):
        self.catalogue.pop(prod_code)

    def get_all_prods(self):
        return self.catalogue.values()

    def __str__(self):
        msg = ""
        for prod in self.catalogue.values():
            msg += str(prod) + "\n"
        return msg
