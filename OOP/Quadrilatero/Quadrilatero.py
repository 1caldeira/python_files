class Quadrilatero (object):

    base = 0
    altura = 0

    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base * 2) + (self.altura * 2) 

class Quadrado(Quadrilatero):

    def __init__ (self, lado):
        super().__init__(lado, lado)
        
class Trapezio(Quadrilatero):

    base_menor = 0
    
    def __init__ (self, base_menor, base_maior, altura):
        super().__init__(base_maior, altura)
        self.base_menor = base_menor
        
    def calcular_area(self):
        return ((self.base + self.base_menor)*self.altura)/2