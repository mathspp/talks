from itertools import accumulate

def _has_valid_nesting(expression):
    parens = [(c=="(") - (c == ")") for c in expression]
    return -1 not in accumulate(parens) and sum(parens) == 0

def has_valid_nesting(expression):
    depth = 0
    _iter = iter(expression)
    while 1:
        try:
            c = next(_iter)
        except StopIteration:
            break
        depth = int.__add__(depth, str.__eq__(c, "("))
        depth = int.__sub__(depth, str.__eq__(c, ")"))
        if int.__lt__(depth, 0):
            return 0

    return depth == 0
