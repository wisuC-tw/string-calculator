import unittest

from string_calculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):
    def test_should_return_zero_given_empty_string(self):
        result = StringCalculator().add("")
        self.assertEqual(0, result)
    
    def test_should_return_same_number_given_string_of_single_number(self):
        result = StringCalculator().add("1")
        self.assertEqual(1, result)

    def test_should_return_sum_given_string_of_two_numbers(self):
        result = StringCalculator().add("1,2")
        self.assertEqual(3, result)

    def test_should_return_sum_given_string_of_many_numbers(self):
        result = StringCalculator().add("1,2,3,4,30")
        self.assertEqual(40, result)

    def test_should_return_sum_given_string_of_two_numbers_split_by_newline(self):
        result = StringCalculator().add("1\n2")
        self.assertEqual(3, result)

    def test_should_return_sum_given_string_of_numbers_split_by_comma_and_newline(self):
        result = StringCalculator().add("1\n2,3")
        self.assertEqual(6, result)
