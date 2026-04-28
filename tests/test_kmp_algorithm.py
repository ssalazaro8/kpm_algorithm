import unittest
from src.kmp_algorithm import kmp_search


class TestKMPAlgorithm(unittest.TestCase):

    def test_exercise_part_a(self):
        text = "abababaab"
        pattern = "ababaa"
        self.assertTrue(kmp_search(text, pattern))

    def test_exercise_part_b(self):
        text = "abababbaa"
        pattern = "ababaa"
        self.assertFalse(kmp_search(text, pattern))

    def test_simple_match(self):
        text = "xxababaa"
        pattern = "ababaa"
        self.assertTrue(kmp_search(text, pattern))

    def test_no_match(self):
        text = "bbbbbbb"
        pattern = "ababaa"
        self.assertFalse(kmp_search(text, pattern))


if __name__ == "__main__":
    unittest.main()