def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    return max(max_product(s[1:]), s[0]*max_product(s[2:]))

def max_product2(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    result_list = []
    for i in range(len(s)):
        if i == 0:
            result_list[-1:] = 1
        else:
            result_list[-1:] = max(s[i]*(result_list[i-2] if s-2 >=0 else 0), s[i-1])
    return result_list[-1]