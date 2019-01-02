import math
import time


def binary_search(testfunc, minimum=0, maximum=256):
    """
    Performs a binary search within specified range. The supplied
    testfunc must have signature: "f(int):bool". Testfuncion must
    only return TRUE if tested_value is larger than the value we
    are searching for (final result).

    For example:

        def test(tested_value):
            return 52 < tested_value

    """
    num_guesses = __calc_guesses(minimum, maximum)
    midpoint = __calc_midpoint(minimum, maximum)

    for guess in range(1,num_guesses+1):
        go_lower = testfunc(midpoint)

        if guess == num_guesses:
            return midpoint - 1 if go_lower else midpoint
        elif go_lower:
            maximum = midpoint - 1
            midpoint = __calc_midpoint(minimum, maximum)
        else:
            minimum = midpoint
            midpoint = __calc_midpoint(minimum, maximum)


def __calc_midpoint(minimum, maximum):
    return maximum - int((maximum - minimum) / 2)


def __calc_guesses(minimum, maximum):
    return math.ceil(math.log((maximum) - minimum, 2.0))