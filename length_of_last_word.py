# https://leetcode.com/problems/length-of-last-word/
def length_of_last_word(str):
    """ Return the length of the last word in the string.
    >>> length_of_last_word("Hello World")
    5

    >>> length_of_last_word("   fly me   to   the moon  ")
    4
    """

    words = str.strip().split()

    return len(words[len(words) - 1])