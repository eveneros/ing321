import unittest

from Labora import labo_4 

class ProbarLabos(unittest.TestCase):
    
    def setUp(self):
        self.ops=labo_4()

    def test_suma(self):
        self.assertEqual(self.ops.suma(3, 5), 8)  # 3 + 5 = 8
        self.assertEqual(self.ops.suma(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(self.ops.suma(0, 0), 0)   # 0 + 0 = 0

    
    def test_factorial(self):
        self.assertEqual(self.ops.factorial(0), 1)       # 0! = 1
        self.assertEqual(self.ops.factorial(1), 1)       # 1! = 1
        self.assertEqual(self.ops.factorial(5), 120)     # 5! = 120


    def test_es_palindromo(self):
        self.assertTrue(self.ops.es_palindromo("anita lava la tina"))  # Es palíndromo
        self.assertTrue(self.ops.es_palindromo("reconocer"))           # Es palíndromo
        self.assertTrue(self.ops.es_palindromo("python"))             # No es palíndromo

if __name__ == '__main__':
    unittest.main()
