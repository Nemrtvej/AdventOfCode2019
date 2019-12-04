from unittest import TestCase
from .main import process_input

class Test(TestCase):

    def test(self):
        cases = [
            ('1,0,0,0,99', '2,0,0,0,99', 2),
            ('2,3,0,3,99', '2,3,0,6,99', 2),
            ('2,4,4,5,99,0', '2,4,4,5,99,9801', 2),
            ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99', 30),
            ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50', 3500),
        ]

        for case in cases:
            test_input, expected_content, expected_result = case
            result_memory = process_input(test_input)
            actual_content = result_memory.serialize()
            actual_result = result_memory.get_result()
            self.assertEqual(expected_content, actual_content)
            self.assertEqual(expected_result, actual_result)