# https://leetcode.com/problems/find-the-highest-altitude/

def find_the_highest_altitude(gain):
    """ You are given an integer array gain of length n where gain[i] is the net
    gain in altitude between points i and i + 1 for all 0 <= i < n. Return the
    highest altitude of a point.

    >>> find_the_highest_altitude([-5,1,5,0,-7])
    1

    >>> find_the_highest_altitude([-4,-3,-2,-1,4,3,2])
    0
    """

    max = 0
    curr = 0

    for i in gain:
        curr += i

        if (curr > max):
            max = curr

    return max