'''Entre com uma sequencia de no mínimo 5 números reais, calcule a média ponderada,
utilizando 0.3 para os dois primeiros valores e para os dois últimos valores, e a 0.1 para
os valores intermediários, exiba o resultado. '''

from Media import Media

nums = list(map(float, input().split()))


m = Media(nums)

print(m.mediaPonderada())
