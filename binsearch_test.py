from binsearch import binary_search
import string
import time
import unittest


class BinarySearchTestcases(unittest.TestCase):

    @staticmethod
    def __make_testfn(secret_value):
        def test(tested_value):
            return secret_value < tested_value
        return test

    def test_binsearch_with_negative_range(self):
        for expected in range(-256,257):
            testfn = BinarySearchTestcases.__make_testfn(expected)
            result = binary_search(testfn, -257, 257)
            self.assertEqual(result, expected)

    def test_binsearch_with_ascii_range(self):
        for character in string.printable:
            expected = ord(character)
            testfn = BinarySearchTestcases.__make_testfn(expected)
            result = binary_search(testfn, 9, 128)
            self.assertEqual(result, expected)

    @staticmethod
    def manual_binsearch():
        print("Think of a number between 0 and 100.")
        print("I will guess it after you answer 7 simple yes/no questions.")

        qnum = 0
        def manual_testfn(tested_value):
            nonlocal qnum
            qnum += 1
            for _ in range(0,3):
                question = str(qnum) + ": Is your number lower than "+str(tested_value)+"? [y/n]: "
                input_var = input(question)
                if input_var.lower().startswith('y'):
                    return True
                if input_var.lower().startswith('n'):
                    return False
                else:
                    print("Invalid answer. Please answer y or n.")
            print("Too many invalid answers were given. Exitting..")
            exit()

        result = binary_search(manual_testfn, 0, 100)
        print("Your number was " + str(result))


#BinarySearchTestcases.manual_binsearch()

if __name__ == '__main__':
    unittest.main()

