inventory = 0 
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or type 'quit' to stop): ")

    if stock.lower() == "quit":
        break

    if stock.startswith("-"):
        if stock[1:].isdigit():
            print("Error: Stock quantity cannot be negative.")
            failed_entries += 1
            continue

        else:
            print("Error: Please enter a valid integer.")
            failed_entries += 1 
            continue
    
    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    stock = int(stock)
    inventory += stock

    if inventory > 500: 
        print("Alert: Inventory is more than 500 units.")
        break

print("Total units Processed:", inventory)
print("Number of Failed Entries:", failed_entries)