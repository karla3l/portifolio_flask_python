""" Usando Python crie uma classe que modele um triangulo:
– Atributos: LadoA, LadoB, LadoC
– Métodos: calcular Perímetro, getMaiorLado;  
Crie um programa que uFlize esta classe. Ele deve pedir ao usuário que informe as medidas de um 
triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado. """

import math
class Triangulo:
    def __init__(self):
        self.ladoA=0
        self.ladoB=0
        self.ladoC=0
        
    def getPerimetro(self):
        return self.ladoA+self.ladoB+self.ladoC
        
    
    def getMaiorLado(self):
        max(self.ladoA, self.ladoB, self.ladoC)
    def getArea(self):
        perimetro = int(self.getPerimetro/2)
        p = perimetro
        A   = self.ladoA
        B  = self.ladoB
        C   = self.ladoC
        area = math.sqrt(p*(p-A)*(p-B)*(p-C))
        return float(f"{area:2f}")
    

    
        
        
