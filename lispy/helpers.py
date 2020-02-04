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


def convert(arg):
    """Recognise the type of argument and convert part of string
    equation according to this type."""

    if (arg[0] == '"') and (arg[-1] == '"'):
        return _str_arg(arg)

    try:
        return int(arg)
    except ValueError:
        pass

    try:
        return float(arg)
    except ValueError:
        pass

    return arg


def brush_equ(equ):
    """Brush equation to make it correct."""
    return equ.strip().replace("\n", " ")


def _str_arg(arg):
    """Get string argument between the quotes."""
    assert len(arg) > 1

    sarg = arg[1:-1]
    sarg = sarg.replace("\\n", "\n")
    sarg = sarg.replace("\\t", "\t")
    return sarg
