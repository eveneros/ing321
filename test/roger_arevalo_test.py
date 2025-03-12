import unittest
from mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_suma(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_suma(), 10, 'La suma tiene error.')

    def test_resta(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_resta(), 10, "la resta es" )
    
    def test_multiplicacion(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_multiplicacion(), 10, " la multiplicacion es ")

    def test_division(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_division(), 10, " la division es ")
   

if __name__ == '__main__':
    unittest.main()

