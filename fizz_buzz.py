# https://leetcode.com/problems/palindrome-number/
def fizz_buzz(n):
    """ Given an integer n, return a string array answer (1-indexed) where:

        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.

    >>> fizz_buzz(3)
    ['1', '2', 'Fizz']

    >>> fizz_buzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    """

    lst = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append("FizzBuzz")
        elif i % 3 == 0:
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else:
            lst.append(str(i))

    return lst