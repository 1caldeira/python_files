'''Entre com uma sequencia de números reais em uma linha, e exiba na tela uma linha com
o fatorial de cada número da sequencia digitada.'''

lista = list(map(float, input().split()))

fat = lambda x : x * fat(x-1) if x > 0 else 1

print(list(map(fat, lista)))

