
from digital_product import DigitalProduct
from supplier import Supplier

# Create a supplier
supplier = Supplier("S002", "Game Supplier", "games@example.com")

# Create a digital product
product2 = DigitalProduct(
    "D001", "Minecraft", 39.90, 100, 1500, supplier
)

# Test the methods
product2.display_information()
print(product2.get_fulfilment_info())
