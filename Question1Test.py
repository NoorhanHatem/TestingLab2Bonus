import unittest
import Question1

class test1(unittest.TestCase):
    def test_even(self):
        self.assertEqual(Question1.checkEvenAndOdd(2), "Even")
        self.assertEqual(Question1.checkEvenAndOdd(100), "Even")
        self.assertEqual(Question1.checkEvenAndOdd(-8), "Even")
        self.assertEqual(Question1.checkEvenAndOdd(46), "Even")

    def test_odd(self):
        self.assertEqual(Question1.checkEvenAndOdd(1), "Odd")
        self.assertEqual(Question1.checkEvenAndOdd(21), "Odd")
        self.assertEqual(Question1.checkEvenAndOdd(33), "Odd")
        self.assertEqual(Question1.checkEvenAndOdd(-57), "Odd")

