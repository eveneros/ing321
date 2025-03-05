import unittest
from mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_multi(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_multiplicacion(), 16, 'El producto fallo.')
        

    def test_resta(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_resta(), 14, 'La resta fallo.')

    def test_division(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_division(), 4, 'El division fallo.')


if __name__ == '__main__':
    unittest.main()