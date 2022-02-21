import time

hoje = time.localtime(time.time())

nome = input("qual seu nome?: ")
meses = ["Janeiro", "Fevereiro", "Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
ano, mes, dia, hora, minuto, segundo = hoje[0],hoje[1],hoje[2],hoje[3],hoje[4],hoje[5]
mes = meses[mes-1]
print("Olá {nome}, hoje é dia {dia} de {mes} de {ano}".format(nome=nome,dia=dia,mes=mes,ano=ano))

while True:
    hoje = time.localtime(time.time())
    hora, minuto, segundo = hoje[3],hoje[4],hoje[5]
    time.sleep(0.5)
    if segundo == 0:
        print("Agora são {hora}:{minuto}".format(hora=hora,minuto=minuto))
        time.sleep(59)