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
