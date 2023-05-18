lista = input().split(" ")
lista = [int(elemento) for elemento in lista]
par = lambda x: x % 2 == 0
impar = lambda x: x % 2 != 0
print(list(filter(par, lista)))
print(list(filter(impar, lista)))