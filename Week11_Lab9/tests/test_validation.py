
import unittest

from product_factory import ProductFactory
from supplier import Supplier
from orderline import OrderLine


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

        self.product = ProductFactory.create(
            "physical", "P001", "Laptop",
            1200.0, 10, self.supplier,
            weight=2.5
        )

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Keyboard",
                -50.0, 10, self.supplier
            )

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Keyboard",
                0.0, 10, self.supplier
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Keyboard",
                50.0, -5, self.supplier
            )

    def test_negative_stock_update(self):
        with self.assertRaises(ValueError):
            self.product.update_stock(-5)

    def test_zero_stock_allowed(self):
        product = ProductFactory.create(
            "physical", "P003", "Mouse",
            25.0, 0, self.supplier
        )
        self.assertEqual(product.to_dict()["stock"], 0)

    def test_zero_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)

    def test_negative_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, -3)

    def test_valid_order_quantity(self):
        line = OrderLine(self.product, 2)
        self.assertAlmostEqual(
            line.calculate_subtotal(), 2400.0
        )

    def test_digital_product_validation(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital", "D001", "Minecraft",
                39.90, -5, self.supplier
            )


if __name__ == "__main__":
    unittest.main()

