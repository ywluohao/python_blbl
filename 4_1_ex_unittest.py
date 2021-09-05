#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import unittest

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    """
    return sum(values) / len(values)


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.1)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
