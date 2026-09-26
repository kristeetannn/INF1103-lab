# #basic structure
# def get_valid_input():
#     # prompt + validation
#     return value


# def process_delivery(current_total, new_value):
#     # calculate new total
#     return new_total


# def calculate_tax(amount):
#     # calculate 10% tax
#     return tax


# def generate_report(total_units, failed_attempts):
#     # print summary
#     pass

import json

failed_attempts = 0


def get_valid_input():
    global failed_attempts

    while True:
        user_input = input("Enter stock quantity or 'quit': ")

        if user_input.lower() == "quit":
            return "quit"

        if user_input.isdigit():
            value = int(user_input)

            if value >= 0:
                return value

        failed_attempts += 1
        print("Invalid input. Please enter a positive integer or 'quit'.")


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts, transaction_history):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Transaction History:", transaction_history)

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            data = json.load(file)

            inventory = data["inventory"]
            transaction_history = data["transaction_history"]

            return inventory, transaction_history

    except FileNotFoundError:
        return 0, []

def save_inventory(inventory, transaction_history):
    data = {
        "inventory": inventory,
        "transaction_history": transaction_history
    }

    with open("inventory.txt", "w") as file:
        json.dump(data, file)

def main():
    global failed_attempts

    inventory, transaction_history = load_inventory()
    deliveries_processed = 0

    print("\nCurrent Inventory:", inventory)
    print("Transaction History:")

    for transaction in transaction_history:
        print(transaction)

    while True:
        value = get_valid_input()

        if value == "quit":
            save_inventory(inventory, transaction_history)
            print("\nInventory successfully saved to inventory.txt.")
            break

        tax = calculate_tax(value)
        inventory = process_delivery(inventory, value)

        transaction_history.append(value)

        deliveries_processed += 1

        print("\nNew transaction added:")
        print(value)
        print("Tax:", tax)
        print("Current Inventory:", inventory)

    generate_report(
        deliveries_processed,
        failed_attempts,
        transaction_history
    )

if __name__ == "__main__":
    main()