<<<<<<< HEAD
def busqueda_lineal (lista,elemento):
    for i in range(len(lista)):
        if lista[i]== elemento:
            return i
    return-1
numeros =[10,20,13,40,50]
#buscar un elemento
elemento_buscado=int(input("ingresa el numero a buscar"))
indice=busqueda_lineal(numeros,elemento_buscado)

if indice !=-1:
    print(f"El numero{elemento_buscado}se encuentra en el indice{indice}")
else: 
    print(f"el numero{elemento_buscado} no se encuetra en la lista")
=======
def busqueda_linea(lista,elementos):
    for i in range(len(lista)):
        if lista[i]==elemento:
            return i
    return-1
numeros =[10,20,13,40,50]
#buscar un elemento
elemento_buscado=int(input("ingresa el numero a buscar"))
indice=busqueda_linea(numeros,elemento_buscado)

if indice !=-1:
    print(f"El numero{elemento_buscado}se encuentra en el indice{indice}")
else: 
    print(f"el numero{elemento_buscado} no se encuetra en la lista")
>>>>>>> 3234736d2c25ed2febff9253b52826c6b41a8dc2
