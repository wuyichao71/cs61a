from LinkLists import *

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    result = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        result *= lnk.first
    a_lnk = Link(result, multiply_lnks([l.rest for l in lst_of_lnks]))
    return a_lnk
