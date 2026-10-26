
import json
from product import Product
from inventory import Inventory

# Create an inventory
inventory = Inventory()

# Load previous inventory data
try:
    with open("inventory.json", "r") as file:
        data = json.load(file)

        for item in data:
            product = Product(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

except FileNotFoundError:
    print("No saved inventory found.")

# Main program
while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        inventory.display_all()

    elif choice == "2":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")

        try:
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))

            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "3":
        product_id = input("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            try:
                stock = int(input("Enter new stock: "))
                product.update_stock(stock)
            except ValueError:
                print("Invalid stock quantity.")
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            product.display_information()
        else:
            print("Product not found.")

    elif choice == "5":
        data = []

        for product in inventory.get_products():
            data.append(product.to_dict())

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully!")

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")

