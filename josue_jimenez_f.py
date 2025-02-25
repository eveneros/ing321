def b_lin(list,elem):
    for i in range(len(list)):
        if list[i]== elem:
            return i
    return -1

num=[1,2,3,4,5]
element=int(input("Elemento:"))
indice= b_lin(num,element)
if indice!= -1:
    print("el numero:",element,"se encuentra em el indice",indice)
else:
    print("el numero:",element,"no se encuentra")

