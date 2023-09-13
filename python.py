# https://leetcode.com/problems/palindrome-number/
def isPalindrome(num):
    """ Check if an integer is a palindrome.
    >>> isPalindrome(121)
    True

    >>> isPalindrome(123)
    False
    """
    string = str(num)
    return string == string[::-1]