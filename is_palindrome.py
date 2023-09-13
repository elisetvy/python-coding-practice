# https://leetcode.com/problems/palindrome-number/
def is_palindrome(num):
    """ Check if an integer is a palindrome.
    >>> is_palindrome(121)
    True

    >>> is_palindrome(123)
    False
    """

    string = str(num)
    return string == string[::-1]