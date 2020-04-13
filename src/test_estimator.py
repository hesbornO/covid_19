
import unittest
from unittest.mock import patch
import math

class TestPower(unittest.TestCase):
    def test_divide(self):             
        self.assertEqual(math.pow(2, 3), 8)        
        
       
if __name__ == '__main__':
    unittest.main()