# hhttps://leetcode.com/problems/remove-element/
def remove_element(nums, val):
    """ Remove all occurences of val from nums in-place. Return the number of
    elements in nums which are not equal to val.
    >>> remove_element([3, 2, 2, 3], 3)
    2

    >>> remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
    5
    """
    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    return len(nums)