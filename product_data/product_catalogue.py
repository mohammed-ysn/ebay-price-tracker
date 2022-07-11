class ProductCatalogue:
    def __init__(self, *prods):
        # k: product id
        # v: product obj
        self.catalogue = {}
        for prod in prods:
            self.catalogue[prod.id] = prod

    def sample_all_prods(self):
        for prod in self.catalogue.values():
            prod.sample_price()

    def sample_prod(self, prod_code):
        self.catalogue[prod_code].sample_price()

    def remove_prod(self, prod_code):
        self.catalogue.pop(prod_code)

    def get_prod(self, code):
        return self.catalogue[code]

    def get_all_prods(self):
        return self.catalogue.values()

    def __str__(self):
        msg = ""
        for prod in self.catalogue.values():
            msg += str(prod) + "\n"
        return msg
