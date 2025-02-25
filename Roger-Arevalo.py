def b-lin(lista.elem):
    for i in range(len(lsita)):
        if lista[i] == elem:
            return 1
    return -1

num = [1,2,3,4,5]
elem = int(input("ingresar el numero a buscar "))
indice = b-lin( num, elem)

if indice != -1:
    print("el numero ",elem," se encuentra en el indice ",indice)
else
    print("el numero ",elem," no se encuentra en la lista")


