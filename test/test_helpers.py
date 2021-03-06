import unittest

from lispy.helpers import split
from lispy.helpers import convert
from lispy.helpers import brush_equ


class TestSplit(unittest.TestCase):
    def test_wrong_equ_no_brackets(self):
        with self.assertRaises(ValueError):
            split("+ 1 2")

    def test_wrong_equ_no_right_bracket(self):
        try:
            split("(+ 1 2")
        except ValueError:
            pass
        else:
            self.assertTrue(False)

    def test_wrong_equ_no_left_bracket(self):
        try:
            split("+ 1 2)")
        except ValueError:
            pass
        else:
            self.assertTrue(False)

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

    def test_trailing_space(self):
        equ = "(+ 1 2 )"
        ps = split(equ)
        self.assertEqual(ps, ["+", "1", "2"])

    def test_trailing_more_spaces(self):
        equ = "(    +       1        2     )"
        ps = split(equ)
        self.assertEqual(ps, ["+", "1", "2"])


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


class TestBrushEqu(unittest.TestCase):
    def test_nothing_to_brush(self):
        self.assertEqual(brush_equ('(+ 1 2)'), '(+ 1 2)')

    def test_remove_single_new_line(self):
        self.assertEqual(brush_equ('(+ 1\n2)'), '(+ 1 2)')

    def test_remove_double_new_line(self):
        self.assertEqual(brush_equ('(+ 1\n\n2)'), '(+ 1  2)')
