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


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def main():
    global failed_attempts

    inventory = 0
    deliveries_processed = 0

    while True:
        value = get_valid_input()

        if value == "quit":
            break

        tax = calculate_tax(value)
        inventory = process_delivery(inventory, value)

        deliveries_processed += 1

        print("Delivery:", value)
        print("Tax:", tax)
        print("Current Inventory:", inventory)

    generate_report(deliveries_processed, failed_attempts)


if __name__ == "__main__":
    main()