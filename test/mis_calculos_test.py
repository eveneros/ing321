import unittest
from mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_suma(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_suma(), 11, 'La suma tiene error.')

<<<<<<< HEAD
    def test_resta(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_resta(), 11, 'La resta tiene error.')

    def test_multiplicacion(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_multiplicacion(), 11, 'La multiplicasion tiene error.')

    def test_division(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_division(), 11, 'La division tiene error.')

            
=======
>>>>>>> b4c95ff74cd27189e320ab6eb2ab91511e91e891
if __name__ == '__main__':
    unittest.main()
