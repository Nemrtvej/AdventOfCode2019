from unittest import TestCase
from day_01.main import calc, calc_with_fuel

class TestDay01(TestCase):

    def test_case_1(self):
        cases = [
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583),
        ]

        for case in cases:
            test_input, expected_result = case
            actual_result = calc(test_input)
            self.assertEqual(expected_result, actual_result)

    def test_case_2(self):
        cases = [
            (100756, 50346),
            (1969, 966),
        ]

        for case in cases:
            test_input, expected_result = case
            actual_result = calc_with_fuel(test_input)
            self.assertEqual(expected_result, actual_result)

