class labo_4:
    

    
    def suma(self, a, b):
        return a + b

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "") 
        return cadena == cadena[::-1]
