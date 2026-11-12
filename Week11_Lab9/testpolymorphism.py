from product_factory import ProductFactory

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "Apple Distributor", "apple@example.com")

physical = ProductFactory.create("physical", "P001", "iPhone", 1200.0, 10, supplier, weight=0.5)
digital = ProductFactory.create("digital", "D001", "Software", 50.0, 20, supplier, download_size=500.0)

inventory = Inventory()

inventory.add_product(physical)
inventory.add_product(digital)

print("\n=== POLYMORPHISM TEST ===")

for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print("--------------------")
