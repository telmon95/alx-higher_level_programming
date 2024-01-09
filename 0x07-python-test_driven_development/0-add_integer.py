#!/usr/bin/python3
"""Module for add_integer"""

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: the first integer.
        b: the second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of the two integers.
    """

    try:
        a = int(a)
        b = int(b)

    except(ValueError, TypeError):
        raise TypeError('a & b must be integers')
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
