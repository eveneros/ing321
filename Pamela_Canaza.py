#algoritmo de busqueda linal
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
         if lista [i] == elemento:
             return i #devuelve el indice
    return -1 #devuele -1 si el elemento no se encuentra

#lista de ejemplo
numeros = [10,20,30,40,50]

#buscar un elemento
elemento_buscado = int(input("ingresa el numero a buscar: "))
indice = busqueda_lineal(numeros, elemento_buscado)

if indice != -1:
    print(f"el numero {elemento_buscado} se encuentra en el indice {indice}")
else:
    print(f"el numero {elemento_buscado} no se encuentra en la lista")