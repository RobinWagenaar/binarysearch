# Binarysearch
This is a python implementation of a uniform binary search algoritm. But instead of classic array searching, it it looks for an integer value within a given range. 

It's basically a programmatic version of the childs game 'Guess my number'. One person thinks of a number below 100 and the other one tries to guess it with 7 simple yes/now questions. You can try it by calling BinarySearchTestcases.manual_binsearch().

```
> python -i
>>> from binsearch_test import BinarySearchTestcases
>>> BinarySearchTestcases.manual_binsearch()
Think of a number between 0 and 100.
I will guess it after you answer 7 simple yes/no questions.
1: Is your number lower than 50? [y/n]: n
2: Is your number lower than 75? [y/n]: y
3: Is your number lower than 62? [y/n]: n
4: Is your number lower than 68? [y/n]: y
5: Is your number lower than 65? [y/n]: n
6: Is your number lower than 66? [y/n]: n
7: Is your number lower than 67? [y/n]: n
Your number was 67
```

# Example code
```python
from binsearch import binary_search
  
def test(guessed_value):
    secret_value = 42
    return secret_value < guessed_value  
    
result = binary_search(test, 0, 100)
print(result); # 42...
```

# Running the tests
I've included a couple of tests, which you can run with this command:
```bash
> python -m unittest binsearch_test.py -v
test_binsearch_with_ascii_range (binsearch_test.BinarySearchTestcases) ... ok
test_binsearch_with_negative_range (binsearch_test.BinarySearchTestcases) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

# How is binary search useful?
Just by itself, it is not. The example above already shows the secret_value, 
so there is no need to deduce it. But there are certain scenario's where one 
might not actually know the secret_value. Then this little algorithm gets 
radically more interesting. 

A real world example can be found [here](https://github.com/RobinWagenaar/binarysearch/blob/master/USAGE.md). 