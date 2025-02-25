def busqueda_lineal(lista,elemmento):
    for i in range(len(lista)):
        if lista[i] == elemmento:
            return i
        return-1
numeros = [10,20,30,40,50]

elemento_buscado = int(input("ingresa el numero a buscar"))
indice = busqueda_lineal(numeros,elemento_buscado)

if indice != -1:
   print(f"El numero{elemento_buscado}se encuentra en el indice{indice}")
else:
    print(f"el numero{elemento_buscado}no se encuentra en la lista")