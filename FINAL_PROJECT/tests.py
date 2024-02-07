import unittest
from for_tests_only import validate_input, sort_sequence


class TestSortingProgram(unittest.TestCase):

    def test_validate_input_valid_values(self):
        valid_values = "3, 1, 4, 1, 5, 9"
        self.assertTrue(validate_input(valid_values))

    def test_validate_input_invalid_values(self):
        invalid_values = "3, 1, 4, a, 5, 9"
        self.assertFalse(validate_input(invalid_values))

    def test_sort_sequence_ascending_order(self):
        sequence = "3, 1, 4, 1, 5, 9"
        sort_order = "Ascending"
        sort_sequence(sequence, sort_order)

    def test_sort_sequence_descending_order(self):
        sequence = "3, 1, 4, 1, 5, 9"
        sort_order = "Descending"
        sort_sequence(sequence, sort_order)


if __name__ == '__main__':
    unittest.main()
