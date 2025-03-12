import unittest
from test.mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_suma(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_suma(), 10, 'La suma tiene error.')
    def test_resta(self):
        calculos = Calculos(8,6)
        self.assertEqual(calculos.get_resta(),2,"La resta tiene error")
    def test_multiplicacion(self):
        calculos = Calculos(8,6)
        self.assertEqual(calculos.get_multiplicacion(),48, "La multiplicacion tiene error")
    def test_division(self):
        calculos = Calculos(12,4)
        self.assertEqual(calculos.get_division(),3, "La multiplicacion tiene error")
if __name__ == '__main__':
    unittest.main()