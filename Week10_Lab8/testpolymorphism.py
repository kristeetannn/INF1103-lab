
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "Apple Distributor", "apple@example.com")

physical = PhysicalProduct("P001", "iPhone", 1200.0, 10, 0.5, supplier)
digital = DigitalProduct("D001", "Software", 50.0, 20, 500.0, supplier)

inventory = Inventory()

inventory.add_product(physical)
inventory.add_product(digital)

print("\n=== POLYMORPHISM TEST ===")

for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print("--------------------")
