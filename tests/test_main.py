import unittest
from searches import binSearch
from searches import interpolSearch
from searches import fibSearch

class TestBinSearch(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(binSearch([2, 3, 4, 5], 3), [3])
        self.assertEqual(binSearch([2, 3, 4, 5], 4), [3, 4])
        self.assertEqual(binSearch([2, 3, 4, 5], 2), [3, 2])
        self.assertEqual(binSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), [5, 8])
        self.assertEqual(binSearch([1, 2], 1), [1])
        self.assertEqual(binSearch([1, 2], 2), [1, 2])
        self.assertEqual(binSearch([1, 3, 3, 4, 5, 6, 7, 8, 9], 1), [5, 3, 1])
    def test_corner(self):
        self.assertEqual(binSearch([2], 2), [2])
        self.assertEqual(binSearch([1, 2, 3, 4, 5], 6), None)
        self.assertEqual(binSearch([2, 3, 4, 5], 1), None)
        self.assertEqual(binSearch([1, 4], 3), [1])

class TestInterpolSearch(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(interpolSearch([2, 3, 4, 5], 3), [3])
        self.assertEqual(interpolSearch([2, 3, 4, 5], 4), [4])
        self.assertEqual(interpolSearch([2, 3, 4, 5], 2), [2])
        self.assertEqual(interpolSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), [8])
        self.assertEqual(interpolSearch([1, 2], 1), [1])
        self.assertEqual(interpolSearch([1, 2], 2), [2])
        self.assertEqual(interpolSearch([1, 3, 3, 4, 5, 6, 7, 8, 9], 1), [1])
        self.assertEqual(interpolSearch([1, 4, 7, 8, 10, 17, 21, 23, 26, 32, 36, 40, 41, 43, 44, 47, 49], 8), [7, 8])
    def test_corner(self):
        self.assertEqual(interpolSearch([2], 2), [2])
        self.assertEqual(interpolSearch([1, 2, 3, 4, 5], 6), None)
        self.assertEqual(interpolSearch([2, 3, 4, 5], 1), None)
        self.assertEqual(interpolSearch([2, 4], 3), [2])

class TestFibSearch(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(fibSearch([3, 4, 7, 10, 13, 16, 18, 19], 8), [7, 13, 10])
        self.assertEqual(fibSearch([1, 2], 1), [1])
        self.assertEqual(fibSearch([1, 2], 2), [1, 2])
        self.assertEqual(fibSearch([1, 3, 3, 4, 5, 6, 7, 8, 9], 1), [5, 3, 1])
    def test_corner(self):
        self.assertEqual(fibSearch([2], 2), [2])
        self.assertEqual(fibSearch([1, 2, 3, 4, 5], 6), None)
        self.assertEqual(fibSearch([2, 3, 4, 5], 1), None)
        self.assertEqual(fibSearch([2, 4], 3), [2])