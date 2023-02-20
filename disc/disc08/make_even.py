def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    # t.label = (t.label//2+1)*2
    # for b in t.branches:
        # make_even(b)

    t.label = t.label+1 if t.label%2 else t.label
    for b in t.branches:
        make_even(b)

