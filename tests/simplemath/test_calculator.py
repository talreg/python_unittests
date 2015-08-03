import unittest
from simplemath.calculator import Calculator
class CalculatorTest(unittest.TestCase):
    """docstring for CalculatorTest"""
    def test_mul(self):
        calc=Calculator()
        self.assertTrue(calc.mul(5,1)==5,"5*1")
    def test_div(self):
        calc=Calculator()
        self.assertTrue(calc.div(55,11)==5,"55/11")

if __name__ == '__main__':
    unittest.main()
