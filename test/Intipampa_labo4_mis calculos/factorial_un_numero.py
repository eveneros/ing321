class Factorial:
    def __init__(self):
        pass
 
    def pedir_numero(self):
        self.numero = int(input("Ingrese un número: "))
 
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)
 
    def mostrar_resultado(self):
        self.pedir_numero()
        resultado = self.factorial(self.numero)
        print("El factorial de {}! es: {}".format(self.numero, resultado))
 
    def ejecutar(self):
        self.mostrar_resultado()
 
factorial = Factorial()
factorial.ejecutar()