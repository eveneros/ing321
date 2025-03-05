class Calculos:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_suma(self):
        return self.a + self.b

    def get_resta(self):
        return self.a - self.b

    def get_multiplicacion(self):
        return self.a * self.b

    def get_division(self):
<<<<<<< HEAD
        if self.b == 0:
            return 'Error: División por cero' 
        return self.a / self.b
=======
        return self.a / self.b
    

>>>>>>> 944044aa5857fc7e579cb5fae3d8c2d346af5669
