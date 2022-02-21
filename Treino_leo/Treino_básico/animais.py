from random import random


class animal():
    def __init__(self,nome,velocidade,inteligencia,população):
        self.nome=nome
        self.inteligencia=inteligencia
        self.velocidade=velocidade
        self.vida=100
        self.sorte = random()
        self.população = população
    def morre(self):
        self.população += -1
    def fome(self):
        self.vida += -10
        if self.vida <=0:
            self.morre()       
    def come(self):
        self.vida += 10

class presa(animal):
    def foge(self):
        return((self.velocidade+1.2*self.inteligencia)*self.vida/100+self.sorte*30)
class predador(animal):
    def caça(self):
        return((self.velocidade+1.2*self.inteligencia)*self.vida/100+self.sorte*30)


class dia():
    def __init__(self,caça,caçador):
        self.caça=caça
        self.caçador=caçador
        self.hora = 0
    def caçada(self):
        caçar = self.caçador.caça()
        fugir = self.caça.foge()
        if caçar <= fugir:
            self.caçador.fome()
        else:
            self.caçador.come()
            self.caça.morre()
    def ciclo(self):
        while self.hora <=24:
            self.caçada()
            self.caça.come()
            self.hora+=1
        self.relatorio()
    def relatorio(self):
        print("A população de {caça} no final do dia é de: {N}".format(caça=self.caça.nome, N = self.caça.população))
        print("A população de {caçadores} no final do dia é de: {N}".format(caçadores=self.caçador.nome, N = self.caçador.população))
            
        
lobos = predador(nome ="lobos", velocidade = 5, inteligencia=5, população=10)
coelhos = presa(nome="coelhos",velocidade=8,inteligencia=4,população=1000)

hoje = dia(coelhos,lobos)
hoje.ciclo()