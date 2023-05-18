'''Crie uma classe com um atributo nums, um método maior() que irá retornar o maior
número, um método menor() que irá retornar o menor número. Entre com uma sequencia
numérica de inteiros em uma linha, instancie um objeto, e exiba na tela o retorno dos
métodos maior e menor deste objeto.
'''

from MaiorMenor import MaiorMenor

lista = list(map(int, input().split()))

nums = MaiorMenor(lista)

print(nums.maior())

print(nums.menor())
