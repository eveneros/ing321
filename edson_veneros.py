class Algoritmos:
    def __init__(self):
        pass

    def suma_numeros(self, a, b):
        """Suma de dos numeros, variables a y b"""
        c= a + b
        print(f"resultado: {c}")

    def es_positivo(self, n):
        if n>=0:
            print("Es positivo")
        else:
            print("Es negativo")



algoritmos = Algoritmos()
#algoritmos.suma_numeros(1,2)
algoritmos.es_positivo(-1)



    