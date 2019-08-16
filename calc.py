import argparse

from lispy.solver import Solver


FUNCS = {
    '+': lambda x, y: x + y, 
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x**y,
}


ARGS = {
    'equation': ""
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("equ", help="Equation to be solved")
    args = parser.parse_args()
    ARGS['equation'] = args.equ


def main():
    parse_args()
    
    s = Solver(FUNCS)
    try:
        r = s(ARGS['equation'])
    except Exception as ex:
        print(ex)
        return

    print(r)

main()
