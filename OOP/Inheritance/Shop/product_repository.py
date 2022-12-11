from Shop.drink import Drink
from Shop.food import Food


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self,product_name):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)

    def __repr__(self):
        result=[]
        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")

        return "\n".join(result)


