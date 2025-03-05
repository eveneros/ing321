import unittest

class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b
    
    def producto(self):
        return self.a * self.b
    
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por 0"
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "")  
        return cadena == cadena[::-1]

class operaciones_test(unittest.TestCase):
    
    def setUp(self):
        
        self.ops = Operaciones(6, 2) 
    
    # Prueba para la función suma
    def test_suma(self):
        self.assertEqual(self.ops.suma(), 8, 'La suma tiene error.')

    def test_resta(self):
        self.assertEqual(self.ops.resta(), 4, 'La resta tiene error.')

    def test_multiplicacion(self):
        self.assertEqual(self.ops.producto(), 12, 'La multiplicación tiene error.')

    def test_division(self):
        self.assertEqual(self.ops.division(), 3, 'La división tiene error.')

    # Prueba para la función factorial
    def test_factorial(self):      
        self.assertEqual(self.ops.factorial(6), 720,"No es su factorial")     

    # Prueba para la función es_palindromo
    def test_es_palindromo(self):
        self.assertTrue(self.ops.es_palindromo("Adán no cede con Eva, Yavé no cede con nada"),"No es palindromo")           
           

if __name__ == "__main__":
    unittest.main()