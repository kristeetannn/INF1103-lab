
import csv

from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)

            # Skip the header row
            next(reader, None)

            for row in reader:
                try:
                    product_type, product_id, name, price, stock = row

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price),
                        int(stock),
                        supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping invalid row: {row}")
                    print(f"Reason: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")

