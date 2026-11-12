
import unittest
from unittest.mock import patch
from tempfile import TemporaryDirectory
from pathlib import Path

from product_loader import load_products
from inventory import Inventory
from supplier import Supplier


class TestLoader(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()

        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

    @patch("builtins.print")
    def test_load_valid_and_invalid_rows(self, mock_print):

        load_products(
            "products.csv",
            self.inventory,
            self.supplier
        )

        products = self.inventory.get_products()

        self.assertEqual(len(products), 3)

        self.assertEqual(
            [p.get_product_id() for p in products],
            ["P001", "D001", "P003"]
        )

        mock_print.assert_any_call(
            "Reason: Unknown product type: service"
        )

        mock_print.assert_any_call("3 products loaded.")
        mock_print.assert_any_call("Load attempt finished.")

    @patch("builtins.print")
    def test_missing_file(self, mock_print):

        with TemporaryDirectory() as folder:
            path = str(Path(folder) / "missing_products.csv")

            load_products(
                path,
                self.inventory,
                self.supplier
            )

            mock_print.assert_any_call(
                f"Products file not found: {path}"
            )

        self.assertEqual(
            len(self.inventory.get_products()), 0
        )

        mock_print.assert_any_call("Load attempt finished.")

    @patch("builtins.print")
    def test_invalid_rows_are_skipped(self, mock_print):

        load_products(
            "products.csv",
            self.inventory,
            self.supplier
        )

        self.assertIsNone(
            self.inventory.find_product("S001")
        )

        self.assertIsNone(
            self.inventory.find_product("P002")
        )

        self.assertIsNotNone(
            self.inventory.find_product("P003")
        )


if __name__ == "__main__":
    unittest.main()

