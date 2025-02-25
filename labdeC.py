def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Devuelve el índice si encuentra el elemento
    return -1  # Si no lo encuentra, devuelve -1 después de recorrer toda la lista

# Ejemplo
numeros = [10, 20, 30, 40, 50]

# Buscar un elemento
elemento_buscado = int(input("Ingresa el número a buscar: "))
indice = busqueda_lineal(numeros, elemento_buscado)

if indice != -1:
    print(f"El número {elemento_buscado} se encuentra en el índice {indice}.")
else:
    print(f"El número {elemento_buscado} no se encuentra en la lista.")
