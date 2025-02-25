def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i 
    return-1 #Devuelve -1 si el elemento no se encuentra

#Lista de ejemplo
numeros = [10, 20, 30, 40, 50]

#Buscar un elemento
elemento_buscado = int(input("Ingresa el número a buscar: "))
indice = busqueda_lineal(numeros, elemento_buscado)

if indice !=-1:
    print(f"El número {elemento_buscado} se encuentra en el indice {indice}.")
else:
    print(f"El numero {elemento_buscado} no se encuentra en la lista.")
