# https://leetcode.com/problems/plus-one/
def plus_one(nums):
    """ Check if an integer is a palindrome.
    >>> plus_one([1, 2, 3])
    [1, 2, 4]

    >>> plus_one([4, 3, 2, 1])
    [4, 3, 2, 2]
    """

    num_string = ''

    for num in nums:
        num_string += str(num)

    num_plus_one = int(num_string) + 1

    l = []

    for num in str(num_plus_one):
        l.append(int(num))

    return l