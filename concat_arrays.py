#https://leetcode.com/problems/concatenation-of-array/
def concat_arrays(nums):
    """ Concats two nums arrays.
    >>> concat_arrays([1, 2, 1])
    [1, 2, 1, 1, 2, 1]

    >>> concat_arrays([1, 3, 2, 1])
    [1, 3, 2, 1, 1, 3, 2, 1]
    """

    return nums + nums