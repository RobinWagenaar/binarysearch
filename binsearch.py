import math
import time


def binary_search(testfunc, minimum=0, maximum=256):
    """
    Performs a binary search within specified range. The supplied
    testfunc must have signature: "f(int):bool". Testfunct must
    only return TRUE if tested_value is larger than the value we
    are searching for (final result).

    For example:

        def test(tested_value):
            return 52 < tested_value

    """
    num_guesses = math.ceil(math.log(maximum - minimum, 2.0))

    for guess in range(1,num_guesses+1):
        midpoint = maximum - int((maximum - minimum) / 2)
        go_lower = testfunc(midpoint)

        if guess == num_guesses:
            return midpoint - 1 if go_lower else midpoint
        elif go_lower:
            maximum = midpoint - 1
        else:
            minimum = midpoint
