
from inventory import Inventory
from supplier import Supplier
from product_loader import load_products


supplier = Supplier(
    "S001", "CSV Supplier", "supplier@example.com"
)

inventory = Inventory()

print("=== TEST 1: Existing CSV File ===")

load_products("products.csv", inventory, supplier)

print("\n=== Loaded Products ===")

inventory.display_all()


print("\n=== TEST 2: Missing CSV File ===")

load_products("missing_products.csv", inventory, supplier)

