"""This module implements helpers for preparing string equations."""


def brush_equ(equ):
    """Brush equation to make it correct."""
    return equ.strip().replace("\n", " ")


def split(equ):
    """Splits equation to parts that can be values or another
    equations. Returns the list of parts."""

    if equ[0] != '(':
        raise ValueError("Syntax error: ( expected")

    if equ[-1] != ')':
        raise ValueError("Syntax error: ) expected")

    _equ = equ[1:-1]

    parts = []
    part = ""
    level = 0
    quote = False

    for sym in _equ:
        if sym == "(":
            level += 1

        if sym == ")":
            level -= 1

        if sym == '"':
            quote = not quote

        if sym == " " and level == 0 and not quote:
            if part:
                parts.append(part)
            part = ""
            continue

        part += sym

    if part:
        parts.append(part)

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


def _str_arg(arg):
    """Get string argument between the quotes."""
    assert len(arg) > 1

    sarg = arg[1:-1]
    sarg = sarg.replace("\\n", "\n")
    sarg = sarg.replace("\\t", "\t")
    return sarg
