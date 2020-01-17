"""This module implements helpers for preparing string equations."""


def split(equ):
    """Splits equation to parts that can be values or another
    equations. Returns list of parts."""

    if equ[0] != '(':
        raise ValueError("Syntax error")
    if equ[-1] != ')':
        raise ValueError("Syntax error")

    _equ = equ[1:-1]

    parts = []
    cur = ""
    level = 0
    quote = False

    for x in _equ:
        if x == "(":
            level += 1

        if x == ")":
            level -= 1

        if x == '"':
            quote = not quote

        if x == " " and level == 0 and not quote:
            if cur:
                parts.append(cur)
            cur = ""
            continue

        cur += x

    if cur:
        parts.append(cur)

    return parts


def convert(x):
    """Recognise the type of argument and convert part of string
    equation according to this type."""
    if x[0] == '"' and x[-1] == '"':
        return x[1:-1]

    try:
        y = int(x)
        return y
    except Exception:
        pass

    try:
        y = float(x)
        return y
    except Exception:
        pass

    return x
