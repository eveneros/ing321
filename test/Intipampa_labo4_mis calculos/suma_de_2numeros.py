class Sumadora:
    def __init__(self):
        pass
 
    def pedir_numeros(self):
        self.num1 = float(input("Ingrese el primer número: "))
        self.num2 = float(input("Ingrese el segundo número: "))
 
    def suma(self, a, b):
        return a + b
 
    def mostrar_resultado(self):
        self.pedir_numeros()
        resultado = self.suma(self.num1, self.num2)
        print("La suma de {} + {} = {}".format(self.num1, self.num2, resultado))
 
    def ejecutar(self):
        self.mostrar_resultado()
 
sumadora = Sumadora()
sumadora.ejecutar()
