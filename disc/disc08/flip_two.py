from LinkLists import *

def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    # if s is Link.empty or s.rest is Link.empty:
    #     return

    # s.first, s.rest.first = s.rest.first, s.first
    # flip_two(s.rest.rest)

    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    while s is not Link.empty and s.rest is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        s = s.rest.rest

