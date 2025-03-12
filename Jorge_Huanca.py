#ALGORITMO DE BUSQUEDA LINEAL
#ESCRIBE UN PROGRAMA QUE BUSQUE UN ELEMENTO EN UNA LISTA USANDO BUSQUEDA LINEAL
 
def busqueda_lineal(lista, elemento):
    for i in range (len(lista)):
        if lista[i]==elemento:
            return i
    return -1
#LISTA DE EJEMPLO
numeros=[10,20,30,40,50]
#BUSCAR UN ELEMENTO
elemento_buscado=int(input("INGRESA EL NUMERO A BUSCAR: "))
indice=busqueda_lineal(numeros,elemento_buscado)
if indice != -1:
    print(f"EL NUMERO {elemento_buscado} SE ENCUENTRA EN EL INDICE {indice}.")
else:
    print(f"EL NUMERO {elemento_buscado} NO SE ENCUENTRA EN LA LISTA.")