import unittest

class Operaciones:
    # 1. Suma de dos números
    def suma(self, a, b):
        return a + b

    # 2. Factorial de un número
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    # 3. Verificar si una cadena es un palíndromo
    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "")  # Ignorar mayúsculas y espacios
        return cadena == cadena[::-1]


class TestOperaciones(unittest.TestCase):
    
    def setUp(self):
        self.ops = Operaciones()
    
    # Prueba para la función suma
    def test_suma(self):
        self.assertEqual(self.ops.suma(3, 5), 8)  # 3 + 5 = 8
        self.assertEqual(self.ops.suma(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(self.ops.suma(0, 0), 0)   # 0 + 0 = 0

    # Prueba para la función factorial
    def test_factorial(self):
        self.assertEqual(self.ops.factorial(0), 1)       # 0! = 1
        self.assertEqual(self.ops.factorial(1), 1)       # 1! = 1
        self.assertEqual(self.ops.factorial(5), 120)     # 5! = 120

    # Prueba para la función es_palindromo
    def test_es_palindromo(self):
        self.assertTrue(self.ops.es_palindromo("anita lava la tina"))  # Es palíndromo
        self.assertTrue(self.ops.es_palindromo("reconocer"))           # Es palíndromo
        self.assertFalse(self.ops.es_palindromo("python"))             # No es palíndromo


# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()