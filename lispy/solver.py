"""This module implements solver."""

from .helpers import split, convert

class Solver:
    def __init__(self, funcs):
        self._funcs = funcs

    def __call__(self, equ):
        parts = split(equ)

        func = parts[0]

        args = []
        for x in parts[1:]:

            if x[0] == "(":
                y = self(x)
            else:
                y = convert(x)

            args.append(y)

        return self._funcs[func](*args)
