
from product import Product


class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
        else:
            self.__products.append(product)
            print("Product added successfully!")

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is not None:
            self.__products.remove(product)
            print("Product removed successfully!")
        else:
            print("Product not found.")

    def display_all(self) -> None:
        if len(self.__products) == 0:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()
                print("--------------------")

    def get_products(self) -> list[Product]:
        return self.__products
