
from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

# Step 1: Create a supplier and a product
supplier = Supplier("S001", "Apple Distributor", "apple@example.com")

iphone = PhysicalProduct(
    "P001", "iPhone", 1200.0, 10, 0.5, supplier
)

# Step 2: Create two separate inventories
inventory_a = Inventory()
inventory_b = Inventory()

# Step 3: Add the product to Inventory A
print("=== INVENTORY A ===")
inventory_a.add_product(iphone)
inventory_a.display_all()

# Step 4: Remove the product from Inventory A
print("\n=== REMOVING PRODUCT ===")
inventory_a.remove_product("P001")

# Step 5: Check whether the product still exists
print("\n=== PRODUCT AFTER REMOVAL ===")
iphone.display_information()

# Step 6: Add the SAME product to Inventory B
print("\n=== INVENTORY B ===")
inventory_b.add_product(iphone)
inventory_b.display_all()

# Step 7: Check that it's the same object
print("\n=== OBJECT IDENTITY CHECK ===")
print(inventory_b.find_product("P001") is iphone)
