
import unittest
from unittest.mock import patch
# import calc
from unittest import mock
from unittest import TestCase


class EstimatorTest(unittest.TestCase):
    # def test_divide(self):             
    #     self.assertEqual(calc.pow(2, 3), 8)
    
    # def test_add(self):             
    #     self.assertEqual(calc.add(10, 5), 15)
    
    # def test_multiply(self):             
    #     self.assertEqual(calc.multiply(10, 5), 50)
        
    # def test_divide(self):             
    #     self.assertEqual(calc.divide(10, 5), 2)
    
    
    def compat_input(self, s=''):
        try:
            return input(s)
        except NameError:
            return input(s)
 
 
 
if __name__ == '__main__':
    unittest.main()