alunos=[("Roberto",10),
        ("Carlos",6),
        ("Marcela",1),
        ("Leticia",10),
        ("Robertinho",0),
        ("Leonardo",7),
        ("Pedro",3),
        ("Luisa",4),
        ("Fabiana",2),
        ("Marcos",5),] 

notas = list(map(lambda x:x[1],alunos))
passados = list(filter(lambda x:x>=6,notas))
def resultado(i):
    if i >= 6:
        return(str(i)+", Aprovado")
    if i<3:
        return(str(i)+", Reprovado")
    else:
        return(str(i)+", Recuperação")


passados2 = [resultado(i) for i in notas]
for i in range(0,len(alunos)):
    passados2[i] = alunos[i][0]+": "+passados2[i] 
print(passados)

for i in passados2:
    print(i)
