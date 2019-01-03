import math
import time


def binary_search(testfn, minimum=0, maximum=256):
    """
    Performs a binary search within specified range. The supplied
    testfn must have signature: "f(int):bool". The testfn must
    only return TRUE if tested_value is larger than the value we
    are searching for (final result).

    For example:

        def test(tested_value):
            return 52 < tested_value

    """
    num_guesses = math.ceil(math.log(maximum - minimum, 2.0))

    for guess in range(1,num_guesses+1):
        midpoint = maximum - int((maximum - minimum) / 2)

        if guess == num_guesses:
            return midpoint - 1 if testfn(midpoint) else midpoint

        if testfn(midpoint):
            maximum = midpoint - 1
        else:
            minimum = midpoint

