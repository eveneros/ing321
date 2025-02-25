def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista [i] == elemento:
            return i
    return -1

numero = [10, 20, 30, 40, 50]

elemento_buscado = int(input("ingrese numero a buscar: "))

indice = busqueda_lineal(numero, elemento_buscado)

if indice != -1:
    print(f"el numero {elemento_buscado} se encuentra en el indice {indice}")

else:
        print(f"el numero {elemento_buscado} no se encuentra en la lista")
