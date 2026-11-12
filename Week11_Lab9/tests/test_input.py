
import unittest
from unittest.mock import patch

from input_helper import get_positive_float


class TestInput(unittest.TestCase):

    @patch("builtins.input", return_value="12.50")
    def test_valid_input(self, mock_input):
        result = get_positive_float("Enter price: ")
        self.assertAlmostEqual(result, 12.50)

    @patch("builtins.input", side_effect=["abc", "-5", "12.50"])
    @patch("builtins.print")
    def test_invalid_input_then_valid(self, mock_print, mock_input):
        result = get_positive_float("Enter price: ")

        self.assertAlmostEqual(result, 12.50)
        self.assertEqual(mock_input.call_count, 3)

        mock_print.assert_any_call(
            "Please enter a valid number, e.g. 12.50"
        )

        mock_print.assert_any_call(
            "Please enter a number greater than zero."
        )

    @patch("builtins.input", side_effect=["0", "25"])
    @patch("builtins.print")
    def test_zero_input(self, mock_print, mock_input):
        result = get_positive_float("Enter price: ")
        self.assertAlmostEqual(result, 25.0)

        mock_print.assert_any_call(
            "Please enter a number greater than zero."
        )


if __name__ == "__main__":
    unittest.main()
