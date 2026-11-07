
from physical_product import PhysicalProduct
from supplier import Supplier

supplier = Supplier("S001", "Laptop Supplier", "laptop@example.com")

product1 = PhysicalProduct(
    "P001", "Laptop", 1200, 15, 2.5, supplier
)

product1.display_information()
print(product1.get_fulfilment_info())
