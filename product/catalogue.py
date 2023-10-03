from typing import Dict, List

from product.abs_product import AbsProduct


class ProductCatalogue:
    def __init__(self, *prods: AbsProduct):
        """Initialise the product catalogue."""
        # k: product id
        # v: product obj
        self.catalogue: Dict[str, AbsProduct] = {}
        for prod in prods:
            self.catalogue[prod.id] = prod

    def sample_all_prods(self) -> None:
        """Sample the price of all products in the catalogue."""
        for prod in self.catalogue.values():
            prod.sample_price()

    def sample_prod(self, prod_id: str) -> None:
        """Sample the price of a product.

        Parameters
        ----------
        prod_id : str
            The product ID.

        """
        self.catalogue[prod_id].sample_price()

    def remove_prod(self, prod_id: str) -> None:
        """Remove a product from the catalogue.

        Parameters
        ----------
        prod_id : str
            The product ID.

        """
        self.catalogue.pop(prod_id)

    def get_prod(self, prod_id: str) -> AbsProduct:
        """Get a product from the catalogue.

        Parameters
        ----------
        prod_id : str
            The product ID.

        Returns
        -------
        AbsProduct
            The product object.

        """
        return self.catalogue[prod_id]

    def get_all_prods(self) -> List[AbsProduct]:
        """Get all of the products in the catalogue.

        Returns
        -------
        List[AbsProduct]
            A list of all of the products.

        """
        return list(self.catalogue.values())

    def __str__(self):
        msg = ""
        for prod in self.catalogue.values():
            msg += str(prod) + "\n"
        return msg
