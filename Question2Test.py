import unittest
import Question2

class test1(unittest.TestCase):
    def test_max(self):
        self.assertEqual(Question2.findMax({2, 5, 1, 0, 9}), 9)
        self.assertEqual(Question2.findMax({99, -99, -100, 56, 80}), 99)
        self.assertEqual(Question2.findMax({-2, -5, -1, 0, -9}), 0)



    def test_min(self):
        self.assertEqual(Question2.findMin({2, 5, 1, 0, 9}), 0)
        self.assertEqual(Question2.findMin({99, -99, -100, 56, 80}), -100)
        self.assertEqual(Question2.findMin({-2, -5, -1, 0, -9}), -9)


