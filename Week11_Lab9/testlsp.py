from product_factory import ProductFactory

from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "Apple Distributor", "apple@example.com")

physical = ProductFactory.create("physical", "P001", "iPhone", 1200.0, 10, supplier, weight=0.5)
digital = ProductFactory.create("digital", "D001", "Software", 50.0, 20, supplier, download_size=500.0)

print("=== PHYSICAL PRODUCT ===")
show_product_details(physical)

print("\n=== DIGITAL PRODUCT ===")
show_product_details(digital)

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

print("\n=== INVENTORY ===")
inventory.display_all()
