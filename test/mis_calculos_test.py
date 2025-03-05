import unittest
from mis_calculos import Calculos

class ProbarCalculos(unittest.TestCase):

    def test_suma(self):
        calculos = Calculos(8, 2)
        self.assertEqual(calculos.get_suma(), 11, 'La suma tiene error.')

    
if __name__ == '__main__':
    unittest.main()