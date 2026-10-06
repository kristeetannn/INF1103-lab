print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

import json


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.\n")

        return inventory

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with default inventory.\n")

        inventory = [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]

        return inventory
    
def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json!\n")

def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("------------------------------------------------\n")


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("\nProduct added successfully!\n")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("\nNew Stock Quantity: "))
            product["stock"] = new_stock

            print("\nStock updated successfully!\n")
            return

    print("Product not found.")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct found")
            print("------------------------------------------------")
            print(
                f"ID: {product['id']}  "
                f"\nName: {product['name']}  "
                f"\nPrice: ${product['price']:.2f}  "
                f"\nStock: {product['stock']}"
            )
            print("------------------------------------------------\n")

            return

    print("\nProduct not found.\n")


# LOAD INVENTORY
inventory = load_inventory()

# PRINT MENU ONLY ONCE
print("----------- MENU -----------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit")
print("----------------------------\n")


# DO NOT PUT THE MENU INSIDE THIS LOOP
while True:

    choice = input("Enter option: ")

    if choice == "1":
        display_all(inventory)

    elif choice == "2":
        add_product(inventory)

    elif choice == "3":
        update_stock(inventory)

    elif choice == "4":
        search_product(inventory)

    elif choice == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)

    elif choice == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)

        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
