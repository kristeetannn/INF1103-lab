
class Inventory:

    def __init__(self):
        self.__products = [] #an empty list

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
        else:
            self.__products.append(product)
            print("Product added successfully!")

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()
                print("--------------------")

    def get_products(self):
        return self.__products

