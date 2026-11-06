
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Step 1: Create one supplier
supplier = Supplier("S001", "Apple Distributor", "apple@example.com")

# Step 2: Create two products using the SAME supplier
physical = PhysicalProduct("P001", "iPhone", 1200.0, 10, 0.5, supplier)
digital = DigitalProduct("D001", "Software", 50.0, 20, 500.0, supplier)

# Step 3: Display both products
print("=== PHYSICAL PRODUCT ===")
physical.display_information()

print("\n=== DIGITAL PRODUCT ===")
digital.display_information()

# Step 4: Delete the local supplier variable
del supplier

# Step 5: Check if products can still access supplier information
print("\n=== AFTER DELETING SUPPLIER VARIABLE ===")
print("Physical supplier:", physical.supplier.name)
print("Digital supplier:", digital.supplier.name)

