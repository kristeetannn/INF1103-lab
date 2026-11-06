
import json
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


# Create inventory object
inventory = Inventory()


# Load saved inventory data
try:
    with open("inventory.json", "r") as file:
        data = json.load(file)

        for item in data:

            # Load supplier information
            supplier_data = item.get("supplier")

            if isinstance(supplier_data, dict):
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )
            else:
                # Support older Lab 7 records without suppliers
                supplier = Supplier(
                    "UNKNOWN", "Unknown Supplier", ""
                )

            if item.get("type") == "physical":
                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"],
                    supplier
                )

            elif item.get("type") == "digital":
                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"],
                    supplier
                )

            else:
                print("Skipping unknown or old product type.")
                continue

            inventory.add_product(product)

except FileNotFoundError:
    print("No saved inventory found.")


# Main menu
while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Create an order")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        inventory.display_all()

    elif choice == "2":
        print("\nSelect product type:")
        print("1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter type (1-2): ")

        if product_type not in ("1", "2"):
            print("Invalid product type.")
            continue

        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")

        # Create Supplier separately from Product
        print("\nEnter supplier information:")
        supplier_id = input("Supplier ID: ")
        supplier_name = input("Supplier name: ")
        supplier_email = input("Supplier email: ")

        supplier = Supplier(
            supplier_id, supplier_name, supplier_email
        )

        try:
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))

            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue

            if product_type == "1":
                weight = float(input("Enter weight (kg): "))

                if weight < 0:
                    print("Weight cannot be negative.")
                    continue

                product = PhysicalProduct(
                    product_id, name, price, stock,
                    weight, supplier
                )

            else:
                download_size = float(
                    input("Enter download size (MB): ")
                )

                if download_size < 0:
                    print("Download size cannot be negative.")
                    continue

                product = DigitalProduct(
                    product_id, name, price, stock,
                    download_size, supplier
                )

            inventory.add_product(product)

        except ValueError:
            print("Invalid number entered.")

    elif choice == "3":
        product_id = input("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            try:
                new_stock = int(input("Enter new stock: "))
                product.update_stock(new_stock)
            except ValueError:
                print("Invalid stock quantity.")
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, PhysicalProduct):
                print(
                    "Shipping Cost: $",
                    product.calculate_shipping_cost()
                )
        else:
            print("Product not found.")

    elif choice == "5":
        data = []

        for product in inventory.get_products():
            product_data = product.to_dict()

            # Save Supplier information alongside Product
            product_data["supplier"] = {
                "supplier_id": product.supplier.supplier_id,
                "name": product.supplier.name,
                "contact_email": product.supplier.contact_email
            }

            data.append(product_data)

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully!")


    elif choice == "6":
        order_id = input("Enter order ID: ")
        order = Order(order_id)

        while True:
            product_id = input(
                "Enter product ID to order (or 'done' to finish): "
            )

            if product_id.lower() == "done":
                break

            product = inventory.find_product(product_id)

            if product is None:
                print("Product not found.")
                continue

            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                order.add_order_line(product, quantity)
                print("Product added to order!")

            except ValueError:
                print("Please enter a valid quantity.")

        print("\n=== ORDER SUMMARY ===")

        for line in order.order_lines:
            print("Product:", line.product.get_product_id())
            print("Quantity:", line.quantity)
            print("Subtotal: $", line.calculate_subtotal())
            print("--------------------")

        print("Order Total: $", order.calculate_total())

    elif choice == "7":
        print("Exiting program.")
        break


    else:
        print("Invalid choice.")
