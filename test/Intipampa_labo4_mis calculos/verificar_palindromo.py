class Palindromo:
    def __init__(self):
        pass
 
    def pedir_cadena(self):
        self.cadena = input("Ingrese una cadena: ")
 
    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "")  # Ignorar mayúsculas y espacios
        return cadena == cadena[::-1]
 
    def mostrar_resultado(self):
        self.pedir_cadena()
        if self.es_palindromo(self.cadena):
            print("La cadena '{}' es un palíndromo.".format(self.cadena))
        else:
            print("La cadena '{}' no es un palíndromo.".format(self.cadena))
 
    def ejecutar(self):
        self.mostrar_resultado()
 
palindromo = Palindromo()
palindromo.ejecutar()
