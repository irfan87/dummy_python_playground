import unittest
import learn_math

class TestLearnMath(unittest.TestCase):
    def test_add(self):
        result = learn_math.add(1, 2)
        self.assertEqual(result, 3)

    def test_substract(self):
        result = learn_math.substract(2, 1)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = learn_math.multiply(2, 2)
        self.assertEqual(result, 4)

    def test_divide(self):
        result = learn_math.divide(4, 2)
        self.assertEqual(result, 2)

        # self.assertRaises(ValueError, learn_math.divide, 10, 0)

        # we can use context manager to run the test
        with self.assertRaises(ValueError):
            learn_math.divide(10, 0)

if __name__ == '__main__':
    unittest.main()