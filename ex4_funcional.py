'''Entre com duas sequencias numéricas de inteiros, cada sequência em uma linha, exiba
na tela o maior número das duas sequências, e o menor número das duas sequencias.'''

lista = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

print(max(lista))

print(min(lista))

print(max(lista2))

print(min(lista2))