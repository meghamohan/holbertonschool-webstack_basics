#!/usr/bin/python3
"""
Unit tests
"""
import unittest
max_integer = __import__('16-max_integer').max_integer

class MaxIntegerTestCases(unittest.TestCase):
    def testEmptyList(self):
        self.assertIsNone(max_integer([]))

    def testNoList(self):
        self.assertEqual(max_integer(), None)

    def testIntList(self):
        self.assertEqual(max_integer([1, 5, 10, 15, 20]), 20)

    def testFlatList(self):
        self.assertEqual(max_integer([1.0, 5.8, 2.8, 11.3, 3]), 11.3)

    def testString(self):
        self.assertEqual(max_integer("megha"), 'm')

    
