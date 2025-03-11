import unittest

class Operaciones:

    def suma(self, a, b):
        return a + b

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "")  
        return cadena == cadena[::-1]

class TestOperaciones(unittest.TestCase):
    
    def setUp(self):
        self.ops = Operaciones()
    

    def test_suma(self):
        self.assertEqual(self.ops.suma(3, 5), 8),"error en la suma" 
        self.assertEqual(self.ops.suma(-1, 1), 0),"Error en la suma "

  
    def test_factorial(self):
        self.assertEqual(self.ops.factorial(0), 1),"ESte no es su factorial"      
        self.assertEqual(self.ops.factorial(1), 1)," este no es su factorial"    


    def test_es_palindromo(self):
        self.assertTrue(self.ops.es_palindromo("anita lava la tina"), "este no es un palindromo")  
        self.assertTrue(self.ops.es_palindromo("reconocer"),"este no es un palindromo")                     

if __name__ == "__main__":
    unittest.main()
