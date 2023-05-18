
class Imovel (object):
    inscricao = 0
    area = 0
    valor_m2 = 0

    def __init__ (self, inscricao, area, valor_m2):
        self.inscricao = inscricao
        self.area = area
        self.valor_m2 = valor_m2
    
    def calcularIPTU(self):
        return self.area*self.valor_m2
    


class Casa (Imovel):
    area_construida = 0
    taxa_construcao = 0
    

    def __init__ (self, inscricao, area, valor_m2, area_construida, taxa_construcao):
        super().__init__(inscricao, area, valor_m2)
        self.area_construida = area_construida
        self.taxa_construcao = taxa_construcao

    def calcularIPTU(self):
        return super().calcularIPTU() + (self.taxa_construcao * self.area_construida)