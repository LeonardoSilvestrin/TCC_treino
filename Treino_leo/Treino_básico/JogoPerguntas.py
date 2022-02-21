import sympy
from sympy.abc import pi
import random
import time
def novo_jogo():
    print(175*'=')
    print(175*'=')
    print("Se desejar parar, basta digitar: \"PARE\" ao invés de responder a pergunta")
    respostas_corretas = 0
    aux_perguntas = dict(perguntas)
    aux_ciclos = 0 #conta quantas perguntas foram feitas
    while True:
        letras = ["A","B","C","D"]
        pergunta = random.choice(list(aux_perguntas.keys()))
        num_pergunta = int(pergunta[0])
        print(175*'=')
        print(pergunta[1:]) 
        print(175*'-')
        aux_letras = 0
        for i in opcoes[num_pergunta-1]:
            print(letras[aux_letras],":",i)
            aux_letras+=1
        print(175*'-')
        resposta = input("Sua resposta (A,B, C ou D): ").upper()
        resposta.replace(" ","")
        time.sleep(0.25)
        if resposta not in letras and resposta != "PARE":
            print("Resposta incorreta, você deve digitar apenas \"A\", \"B\", \"C\",\"D\" ou \"Pare\" se quiser parar de jogar, por favor não digite outras coisas na caixa de resposta")
        elif resposta == perguntas.get(pergunta):
            respostas_corretas+=1
            print("Resposta Correta! :) -- Placar até agora:{k}/{t}".format(k=respostas_corretas,t=aux_ciclos+1))
        elif resposta == "PARE":
            placar(respostas_corretas,aux_ciclos)
            break
        else:
            print("Resposta Errada :( -- Placar até agora:{k}/{t}".format(k=respostas_corretas,t=aux_ciclos+1))
        aux_ciclos +=1
        aux_perguntas.pop(pergunta)
        time.sleep(0.1)
        if aux_perguntas == {}:
            print(175*'=')
            print("Nossa, você respondeu todas as perguntas do nosso banco de dados :O")
            placar(respostas_corretas,aux_ciclos)
            break
def placar(respostas_corretas,aux_ciclos):
    if aux_ciclos == len(perguntas) and respostas_corretas == len(perguntas):
        print("CARALHO TU É O BIXÃO MESMO EM, RESPONDEU TUDO E RESPONDEU TUDO CERTO AINDA, QUEEE ISSO, ACERTOU {k}/{k}.".format(k=len(perguntas)))
    else:
        if respostas_corretas==1:
            s=""
        else:
            s="s"
        print(175*'=')
        print("Você respondeu {r} pergunta{s} corretamente de um total de {t} questões, Parabéns!".format(r=respostas_corretas,t=len(perguntas),s=s))
        print(175*'-')
    desejo = input("Deseja jogar novamente?(s/n): ").lower()
    if desejo == "s":
        print(175*'-')
        print("Ótimo, vamos recomeçar o jogo")
        novo_jogo()
    else:
        print("Obrigado por jogar! até a próxima :)")
perguntas = {
    "1Quem criou o avião?": "A",
    "2Qual a fórmula da área de um circulo de raio \"r\"?": "A",
    "3Qual a maior cidade do mundo em população?":"C",
    "4Quantas letras possui o alfabeto?":"C",
    "5Qual a capital do Brasil?":"D",
    "6Qual a estrela mais próxima do sol?":"B",
    "7Quem pintou a Mona Lisa?":"C"
}
opcoes = [["Santos Dummont","Irmãos Wright","Leonardo DaVinci","Nikola Tesla"],
["{pi}r^2","2{pi}r","2/3{pi}r^4","{pi}^2r"],
["São Paulo","Nova Iorque","Tokyo","Xangai"],
["24","25","26","27"],
["Sâo Paulo", "Rio de Janeiro", "Bahia", "Brasília"],
["Póllux","Proxima Centauri","Alpha Centauri","Beta Centauri"],
["Rafael","Donatello","Leonardo", "Michelangelo"]
]
for elemento in opcoes[1]:
    aux = opcoes[1].index(elemento)
    elemento = elemento.format(pi = sympy.pretty(pi))
    opcoes[1][aux] = elemento
novo_jogo()