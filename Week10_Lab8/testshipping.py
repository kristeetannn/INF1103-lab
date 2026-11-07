
from physical_product import PhysicalProduct
from supplier import Supplier

# Create supplier
supplier = Supplier(
    "S003", "Electronics Supplier", "electronics@example.com"
)

# Create two physical products
product1 = PhysicalProduct(
    "P001", "Laptop", 1200, 15, 2.5, supplier
)

product2 = PhysicalProduct(
    "P002", "Keyboard", 80, 20, 0.8, supplier
)

# Test shipping calculations
print("Laptop Shipping Cost: $", product1.calculate_shipping_cost())
print("Keyboard Shipping Cost: $", product2.calculate_shipping_cost())

# Check the correct results
assert product1.calculate_shipping_cost() == 12.5
assert product2.calculate_shipping_cost() == 4.0

print("PASS: Shipping calculations are correct.")
