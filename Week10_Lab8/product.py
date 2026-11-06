
from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.supplier: Supplier = supplier

    def update_stock(self, quantity: int) -> None:
        if quantity >= 0:
            self.__stock = quantity
            print("Stock updated successfully!")
        else:
            print("Stock cannot be negative.")

    def display_information(self) -> None:
        print("Product ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price:", self.__price)
        print("Stock:", self.__stock)
        print("Supplier:", self.supplier.name)

    def get_product_id(self) -> str:
        return self.__product_id

    def get_price(self) -> float:
        return self.__price

    def to_dict(self) -> dict:
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
