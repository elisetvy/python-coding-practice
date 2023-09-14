# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
def find_index_of_first(str, target):
    """ Remove duplicates from a sorted array in-place. Return the number of unique values.
    >>> find_index_of_first("sadbutsad", "sad")
    0

    >>> find_index_of_first("leetcode", "leeto")
    -1
    """
    i = 0

    while i < len(str):
        substr = str[i::]
        if substr.startswith(target):
            return i
        else:
            i += 1

    return -1