import unittest
from mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_suma(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_suma(), 10, 'La suma tiene error.')

    def test_resta(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_resta(), 6, 'La resta tiene error.')

    def test_multiplicacion(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_multiplicacion(), 16, 'La multiplicación tiene error.')

    def test_division(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_division(), 4, ' La división tiene error.')

    def test_division_por_cero(self):
        calculos = Calculos(8, 0)
        self.assertEqual(calculos.get_division(), 'Error: División por cero', 'La división por cero tiene error.')

if __name__ == '__main__':
    unittest.main()
