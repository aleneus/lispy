import unittest

import sys
import os
sys.path.insert(0, os.path.abspath("."))

from lispy.helpers import split, convert


class TestSplit(unittest.TestCase):
    def test_wrong_equ_no_brackets(self):
        try:
            r = split("+ 1 2")
        except ValueError:
            pass

    def test_flat(self):
        equ = "(+ 1 2)"
        ps = split(equ)
        self.assertEqual(len(ps), 3)
        self.assertEqual(ps[0], "+")
        self.assertEqual(ps[1], "1")
        self.assertEqual(ps[2], "2")

    def test_nested(self):
        equ = "(+ 1 (+ 1 2))"
        ps = split(equ)
        self.assertEqual(len(ps), 3)
        self.assertEqual(ps[0], "+")
        self.assertEqual(ps[1], "1")
        self.assertEqual(ps[2], "(+ 1 2)")


class TestConvert(unittest.TestCase):
    def test_int(self):
        s = "1"
        r = convert(s)
        self.assertTrue(isinstance(r, int))

    def test_float(self):
        s = "1."
        r = convert(s)
        self.assertTrue(isinstance(r, float))

    def test_str(self):
        s = '"1"'
        r = convert(s)
        self.assertTrue(isinstance(r, str))

    def test_default_str(self):
        s = 'int'
        r = convert(s)
        self.assertTrue(isinstance(r, str))


unittest.main()
