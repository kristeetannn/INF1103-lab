from physical_product import PhysicalProduct

product1 = PhysicalProduct("P001", "Laptop", 1200, 15, 2.5)
product2 = PhysicalProduct("P002", "Keyboard", 80, 20, 0.8)

print("Laptop shipping cost: $", product1.calculate_shipping_cost())
print("Keyboard shipping cost: $", product2.calculate_shipping_cost())