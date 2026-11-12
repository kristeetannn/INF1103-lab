
import unittest

from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from supplier import Supplier


class TestFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Laptop",
            1200.0, 10, self.supplier,
            weight=2.5
        )

        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_product_id(), "P001")
        self.assertAlmostEqual(product.calculate_shipping_cost(), 12.5)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Minecraft",
            39.90, 100, self.supplier,
            download_size=1500
        )

        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(product.get_product_id(), "D001")

    def test_returns_product(self):
        product = ProductFactory.create(
            "physical", "P002", "Desk Lamp",
            25.0, 10, self.supplier
        )

        self.assertIsInstance(product, Product)

    def test_unknown_product_type(self):
        with self.assertRaisesRegex(
            ValueError, "Unknown product type: service"
        ):
            ProductFactory.create(
                "service", "S001", "Installation",
                30.0, 5, self.supplier
            )


if __name__ == "__main__":
    unittest.main()

