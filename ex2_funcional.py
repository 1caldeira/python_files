from functools import reduce
lista = input().split(" ")

lista = [int(elemento) for elemento in lista]

par = lambda x: x % 2 == 0

soma = lambda x , y: x+y

lista_par = list(filter(par, lista))

print(reduce(soma, lista_par))