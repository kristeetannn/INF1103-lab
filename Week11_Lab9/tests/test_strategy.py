from product_factory import ProductFactory

import unittest
from order import Order
from supplier import Supplier
from physical_product import PhysicalProduct
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


class TestStrategy(unittest.TestCase):

    def setUp(self):
        supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

        self.product = ProductFactory.create("physical", "P001", "Desk", 250.0, 10, supplier, weight=5.0)

        self.order = Order("O001")
        self.order.add_order_line(self.product, 1)

    def test_default_discount(self):
        self.assertAlmostEqual(
            self.order.calculate_total(), 250.0
        )

    def test_no_discount(self):
        self.order.set_discount(NoDiscount())
        self.assertAlmostEqual(
            self.order.calculate_total(), 250.0
        )

    def test_percentage_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(
            self.order.calculate_total(), 225.0
        )

    def test_bulk_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertAlmostEqual(
            self.order.calculate_total(), 230.0
        )

    def test_bulk_discount_below_threshold(self):
        discount = BulkDiscount(200, 20)
        self.assertAlmostEqual(discount.apply(150), 150)

    def test_student_discount(self):
        self.order.set_discount(StudentDiscount())
        self.assertAlmostEqual(
            self.order.calculate_total(), 237.5
        )

    def test_change_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertAlmostEqual(
            self.order.calculate_total(), 230.0
        )

        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(
            self.order.calculate_total(), 225.0
        )

    def test_constructor_discount(self):
        order = Order("O002", PercentageDiscount(10))
        order.add_order_line(self.product, 1)
        self.assertAlmostEqual(
            order.calculate_total(), 225.0
        )


if __name__ == "__main__":
    unittest.main()

