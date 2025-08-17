from products import Product
from typing import List

class Store:
    """
    A class representing a store that holds multiple products.
    Supports adding/removing products, getting total stock, listing active products,
    and placing orders.
    """

    def __init__(self, products: List[Product] = None):
        """
        Initialize the store with a list of products.
        If no products are given, start with an empty list.
        """
        #self.products = [] if products is None else products.copy()
        if products is None:
            self.products = []
        else:
            for product in products:
                if not isinstance(product, Product):
                    raise TypeError("All items in products list must be Product instances")
            self.products = products.copy()


    def add_product(self, product):
        """Adds a product to the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the store")
        if product not in self.products:
            self.products.append(product)
        self.products.append(product)

    def remove_product(self, product):
        """Checks if a item is in the store and removes it from store if it is."""
        try:
            self.products.remove(product)
        except ValueError:
            print("Product not found in store")

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Buys multiple products.
        shopping_list: list of tuples (product, quantity)
        Returns total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError(f"Invalid Item on shopping list: {product}")
            if not isinstance(quantity, int):
                raise ValueError(f"Invalid quantity {quantity} on product {product.name}")
            total_price += product.buy(quantity)
        return total_price



