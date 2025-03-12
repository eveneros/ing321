def busqueda_lineal(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return -1

num = [1,2,3,4,5]
elem_b = int(input("ingresar el numero a buscar "))
indice = busqueda_lineal( num, elem_b)

if indice != -1:
    print("el numero ",elem_b," se encuentra en el indice ",indice)
else:
    print("el numero ",elem_b," no se encuentra en la lista")


