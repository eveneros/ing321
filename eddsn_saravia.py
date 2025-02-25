#algoritmo de busqueda lineal
def busqueda_lineal(lista, elemnto):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i #develve el indice del elemto encontrado
        return -1 # devuelve -1 si el elemnto no se encuentra

# Listade ejemplo
numeros = [10, 20, 30, 40, 50]

#Buscar un elemento
elemento_buscado = int(input("ingresa el nuero a buscar: "))
indice = busqueda_lineal(numeros,elemento_buscado)

if indice != -1:
    print(f"el numero {elemento_buscado} se encuentra en el indice {indice} ")
else:
    print(f"el numero {elemento_buscado} no s encuentr en la lista.")