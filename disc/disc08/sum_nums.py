from LinkLists import *
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while s is not Link.empty:
        result, s = result+s.first, s.rest
    return result

