#!/usr/bin/python3

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_start(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_mid(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_mixed(self):
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)

    def test_single_negative(self):
        self.assertEqual(max_integer([-1, 2, 3, 4, 5]), 5)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_single_int(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty(self):
        self.assertIsNone(max_integer([]))
