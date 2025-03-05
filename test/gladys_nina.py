import unittest
from mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_suma(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_suma(), 10, 'La suma tiene error.')

    def test_resta(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_resta(), 10, 'La resta tiene error.')
    
    def test_multip(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_multiplicacion(), 16, 'El producto tiene error.')
    
    def test_div(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_division(), 10, 'La div tiene error.')

    
if __name__ == '__main__':
    unittest.main()