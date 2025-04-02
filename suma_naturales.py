import timeit
def suma_iterativa(n):
    suma=0
    for i in range (1,n+1):
        suma+=i
    return suma
def suma_recursiva(n):
    if n==0:
        return 0
    return n + suma_recursiva(n-1)
def suma_formula(n):
    return n*(n+1)//2
n=100
assert suma_iterativa(n)==suma_recursiva(n)==suma_formula(n),"!las formulas no coinciden"
print("todas las sumas dan el mismo resultado")

print("tiempo iterativa:",timeit.timeit(lambda:suma_iterativa(n), number=1000),"segundos")
print("tiempo recursiva:",timeit.timeit(lambda:suma_recursiva(n), number=1000),"segundos")
print("tiempo fromula:",timeit.timeit(lambda:suma_formula(n), number=1000),"segundos")