'''Crie uma classe pai Quadrilatero que possui dois atributos: base e altura, e dois métodos
calcular_area() e calcular_perimetro(). Uma classe filha Quadrado, que em seu
construtor recebe 1 parâmetro que o tamanho do lado do quadrado, e atribui este valor a
base e altura da classe pai, não precisando escrever novamente os métodos. Uma classe
filha Trapezio, posui um atributo base_menor, e seu construtor recebe os parametros
base maior, base menor e altura, e deve sobreescrever o método da classe pai
calcular_area() com o cálculo ((base maior+ base menor)*h)/2. Crie 3 objetos (1 objeto
da classe Quadrilátero, 1 objeto da classe Quadrado, e 1 objeto da classe Trapezeio,
coloque-os em uma lista, e utilizando do polimorfismo calcule a soma dos perimetros e
das área de todos os objetos.'''

from Quadrilatero import *

lista = [Quadrilatero(2,4), Quadrado(3), Trapezio(2,4,5)]

soma = 0

for i in lista:
    soma += i.calcular_area()
    soma += i.calcular_perimetro()

print(soma)