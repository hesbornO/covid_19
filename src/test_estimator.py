
import unittest
from unittest.mock import patch
import math

class TestPower(unittest.TestCase):
    def test_divide(self):             
        self.assertEqual(math.pow(2, 3), 8)
    
    def test_add(self):             
        self.assertEqual(math.add(10, 5), 15)
    
    def test_multiply(self):             
        self.assertEqual(math.multiply(10, 5), 50)
        
    def test_divide(self):             
        self.assertEqual(math.divide(10, 5), 2)
    
    def test_prompt(self, capsys, monkeypatch):
        monkeypatch.setattr('path.to.yourmodule.input', lambda: 'no')
        val = input(bear=..., printer=...)
        assert not val        
        
       
if __name__ == '__main__':
    unittest.main()