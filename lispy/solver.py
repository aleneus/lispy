"""This module implements solver."""

from lispy.helpers import split, convert, brush_equ


class Solver:
    """Solver calculates the lisp equation usin the set of basic
    functions.

    Parameters
    ----------
    funcs: list of functions
        Functions familiar to solver
    """
    def __init__(self, funcs):
        self._funcs = funcs

    def __call__(self, equ):
        equ_norm = brush_equ(equ)
        parts = split(equ_norm)

        func = parts[0]

        args = []
        for x in parts[1:]:

            if x[0] == "(":
                y = self(x)
            else:
                y = convert(x)

            args.append(y)

        return self._funcs[func](*args)
