
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

# Step 1: Create a supplier
supplier = Supplier("S001", "Apple Distributor", "apple@example.com")

# Step 2: Create two products
iphone = PhysicalProduct("P001", "iPhone", 1200.0, 10, 0.5, supplier)
software = DigitalProduct("D001", "Software", 50.0, 20, 500.0, supplier)

# Step 3: Create the first order
order1 = Order("O001")

# Step 4: Add products to the order
order1.add_order_line(iphone, 2)
order1.add_order_line(software, 3)

# Step 5: Display subtotals
print("=== ORDER 1 ===")

for line in order1.order_lines:
    print("Subtotal: $", line.calculate_subtotal())

print("Order 1 Total: $", order1.calculate_total())

# Step 6: Create a second order
order2 = Order("O002")
order2.add_order_line(iphone, 1)

print("\n=== ORDER 2 ===")
print("Order 2 Total: $", order2.calculate_total())

# Step 7: Check object identities
print("\n=== COMPOSITION TEST ===")
print("Same Product:",
      order1.order_lines[0].product is order2.order_lines[0].product)

print("Same OrderLine:",
      order1.order_lines[0] is order2.order_lines[0])

