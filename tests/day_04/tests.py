from unittest import TestCase
from day_04.main import Checker

class TestDay04(TestCase):

    def test_checker_first_version(self):
        cases = [
            ('111111', True),
            ('223450', False),
            ('123789', False),
        ]

        checker = Checker()
        for case in cases:
            test_input, expected_result = case
            actual_result = checker.check_first_version(test_input)
            self.assertEqual(
                expected_result,
                actual_result,
                '%s should be %s but the actual result is %s' % (test_input, expected_result, actual_result)
            )

    def test_checker_second_version(self):
        cases = [
            ('112233', True),
            ('123444', False),
            ('111122', True),
        ]

        checker = Checker()
        for case in cases:
            test_input, expected_result = case
            actual_result = checker.check_second_version(test_input)
            self.assertEqual(
                expected_result,
                actual_result,
                '%s should be %s but the actual result is %s' % (test_input, expected_result, actual_result)
            )