def busqueda_lineal(lista, elemento):
    for i in range (len(lista)):
        if lista [i] == elemento:
            return i
    return -1

numeros = [10, 20, 30, 40, 50]

elemento_buscado = int(input("ingresa el numero a buscar: "))
indice = busqueda_lineal(numeros, elemento_buscado)

if indice != -1:
   print(f"El numero {elemento_buscado} se encuentra en el indice {numeros}")
else:
    print(f"el numero {elemento_buscado} no se encuentra en la lista") 