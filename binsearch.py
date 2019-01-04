import math
import time


def binary_search(testfn, minimum=0, maximum=128):
    """
    Performs a binary search within specified range. The supplied
    testfn must have signature: "f(int):bool". The testfn must
    only return TRUE if secret_value is lower than the value we
    are searching for (tested_value).

    For example:

        def test(tested_value):
            secret_value = 52
            return secret_value < tested_value

    """
    last_guess = math.ceil(math.log(maximum - minimum, 2.0))

    for this_guess in range(1,last_guess+1):
        midpoint = maximum - int((maximum - minimum) / 2)

        if this_guess == last_guess:
            return midpoint - 1 if testfn(midpoint) else midpoint
        elif testfn(midpoint):
            maximum = midpoint - 1
        else:
            minimum = midpoint

