# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums):
    """ Remove duplicates from a sorted array in-place. Return the number of unique values.
    >>> remove_duplicates([2, 2, 3, 3])
    2

    >>> remove_duplicates([0, 1, 2, 2, 3, 4, 4])
    5
    """
    i = 1

    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1

    return len(nums)