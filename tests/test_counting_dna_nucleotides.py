import unittest
from solutions.counting_dna_nucleotides import solve


class TestDNACount(unittest.TestCase):
    def test_something(self):
        input_data = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        expected_output = "20 12 17 21"
        self.assertEqual(solve(input_data), expected_output)

    def test_empty_string(self):
        self.assertEqual(solve(""), "0 0 0 0")

    def test_all_nucleotides(self):
        self.assertEqual(solve("ACGTACGT"), "2 2 2 2")

    def test_fibonacci(self):
        self.assertEqual(solve("ATTTTATCGTTTGGGCTCTAGCGGGTCTT"), "3 5 8 13")

    def test_lower(self):
        self.assertEqual(solve("attggc"), "1 1 2 2")

    def test_mixed(self):
        self.assertEqual(solve("atTgGC"), "1 1 2 2")


if __name__ == '__main__':
    unittest.main()
