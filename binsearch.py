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
    for _ in range(math.ceil(math.log(maximum - minimum, 2.0))):
        midpoint = maximum - int((maximum - minimum) / 2)
        result = testfn(midpoint)
        if result:
            maximum = midpoint - 1
        else:
            minimum = midpoint
    return maximum if result else minimum
