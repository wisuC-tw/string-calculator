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

    def test_should_return_sum_given_string_of_numbers_with_new_format(self):
        result = StringCalculator().add("//;\n1;2")
        self.assertEqual(3, result)

    def test_extract_delimiter_should_split_delimiter_and_number_string(self):
        result = StringCalculator().extract_delimiter("//;\n1;2")
        self.assertEqual((";", "1;2"), result)

    def test_extract_delimiter_should_return_no_delimiter_and_number_string_given_no_delimiter(self):
        result = StringCalculator().extract_delimiter("1,2")
        self.assertEqual(("", "1,2"), result)

    def test_extract_delimiter_should_return_tuple_of_empty_strings_given_empty_input(self):
        result = StringCalculator().extract_delimiter("")
        self.assertEqual(("", ""), result)

    def test_should_parse_default_delimiter(self):
        result = StringCalculator().parse("1\n2,3,4\n5,66")
        self.assertEqual(["1", "2", "3", "4", "5", "66"], result)

    def test_should_parse_semicolon_delimiter(self):
        result = StringCalculator().parse("1;2;3", ";")
        self.assertEqual(["1", "2", "3"], result)

    def test_should_return_0_if_no_number_in_input_string(self):
        result = StringCalculator().add("//;\n")
        self.assertEqual(0, result)
