'''Entre com 3 sequencias de números inteiros, uma sequencia em cada linha. Exiba na tela
em uma linha a sequencia dos números em ordem crescente sem números iguais.'''

lista = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
lista3 = list(map(int, input().split()))

listafinal = lista + lista2 + lista3

listafinal = list(set(listafinal))

print(sorted(listafinal))