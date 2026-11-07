
from product import Product
from supplier import Supplier

# Create a supplier
supplier = Supplier("S004", "Test Supplier", "test@example.com")

# Test that an abstract class cannot be instantiated
try:
    product = Product("P003", "Test", 10, 5, supplier)

except TypeError as error:
    if "abstract" in str(error).lower():
        print("PASS: Abstract Product cannot be instantiated.")
    else:
        raise

else:
    raise AssertionError("FAIL: Abstract Product was instantiated.")
