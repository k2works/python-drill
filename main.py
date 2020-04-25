
import doctest


def add(a, b):
    """Return the sum of a and b.

    >>> add(2, 2)
    4
    """
    sum = a + b
    return sum


doctest.testmod(verbose=True)
