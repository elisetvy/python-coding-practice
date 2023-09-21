# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    """ Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.

    >>> two_sum([2,7,11,15], 9)
    [0, 1]

    >>> two_sum([3,2,4], 6)
    [1, 2]
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]