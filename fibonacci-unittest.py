import fibonacci
import unittest

class TestFibonacciFunctions(unittest.TestCase):

    def test_series_100(self):
        print('\nTest Series 100')
        expected_result = [1,1,2,3,5,8,13,21,34,55,89]
        test_result = fibonacci.fibonacci_sequence(11)
        self.assertEqual(expected_result,test_result)

    def test_series_50(self):
        print('\nTest Series 50')
        expected_result = [1,1,2,3,5,8,13,21,34]
        test_result = fibonacci.fibonacci_sequence(9)
        self.assertEqual(expected_result,test_result)

if __name__ == '__main__' :
    unittest.main()
