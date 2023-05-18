from Imovel import Imovel, Casa

def saida(lista):
    sum = 0
    for i in lista:
        print("casa: ", i.inscricao, "| valor iptu:", i.calcularIPTU())
        sum += i.calcularIPTU()

    print("\nsoma dos IPTUs: ", sum,"\n") 

imovel1 = Imovel(1000, 600, 4)
imovel2 = Imovel(1001, 500, 6)
casa1 = Casa(1010, 500.10, 6.50, 300, 6.5)
casa2 = Casa(1011, 600.10, 5.50, 300, 6.7)
casa3 = Casa(1012, 400.10, 3.70, 200, 4.5)

lista = [imovel1, imovel2, casa1, casa2, casa3]
print("\n")
saida(lista)