#Algoritmo de busqueda lineal
def busqueda_lineal (lista, elemento):
    for i in range (len(lista)):
        if lista [i]== elemento:
            return i #devuelve el indice del elemento encontrado
    return -1 #devuelve -1 si el elemento no esta
#lista de ejemplo
numeros =[10, 20, 30, 40, 50]
#Buscar un elemento
elemento_buscado = int(input("Ingresa un numero a buscar: "))
indice = busqueda_lineal(numeros, elemento_buscado)
if indice!=-1:
    print (f"El numero {elemento_buscado} se encuentra en el indice {indice} ")
else:
    print (f"El numero {elemento_buscado} no se encuentra en la lista")