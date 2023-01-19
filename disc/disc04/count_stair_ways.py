def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)