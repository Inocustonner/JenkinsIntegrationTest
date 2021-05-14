import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def testAdding(self):
        self.assertEqual(calculator.adding(1, 3), 4)
        self.assertEqual(calculator.adding(0, 3), 3)
        self.assertEqual(calculator.adding(-1, 3), 2)

if __name__ == '__main__':
    unittest.main()