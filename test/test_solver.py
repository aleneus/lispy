import unittest

from lispy.solver import Solver


FUNCS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'cat': lambda x, y: x + y
}


class TestEval(unittest.TestCase):
    def setUp(self):
        self.solve = Solver(FUNCS)

    def test_sum_1_2(self):
        equ = '(+ 1 2)'
        r = self.solve(equ)
        self.assertEqual(r, 3)

    def test_sum_2_3(self):
        equ = "(+ 2 3)"
        r = self.solve(equ)
        self.assertEqual(r, 5)

    def test_nested(self):
        equ = "(+ (+ 1 1) (- 3 1))"
        r = self.solve(equ)
        self.assertEqual(r, 4)

    def test_more_nested(self):
        equ = "(+ (+ (- 10 9) 1) (- (+ 2 1) (+ (+ 5 -5) 1)))"
        r = self.solve(equ)
        self.assertEqual(r, 4)

    def test_sum_float(self):
        equ = "(+ 1 1.2)"
        r = self.solve(equ)
        self.assertAlmostEqual(r, 2.2)

    def test_wrong_types(self):
        equ = '(+ 1 "q")'
        try:
            self.solve(equ)
        except TypeError:
            pass
        else:
            self.assertTrue(False)

    def test_cat(self):
        equ = '(cat "a" "b")'
        r = self.solve(equ)
        self.assertEqual(r, "ab")

    def test_cat_spaces(self):
        equ = '(cat "a b" " c")'
        r = self.solve(equ)
        self.assertEqual(r, "a b c")

    def test_wrong_func(self):
        equ = '(unknown 1 2)'
        try:
            self.solve(equ)
        except KeyError:
            pass
        else:
            self.assertTrue(False)
