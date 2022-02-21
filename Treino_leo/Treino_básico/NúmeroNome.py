# name = input("Nome Completo:")
# name = name.replace(" ","")
# name = name.upper()
# name = list(name)
# alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# n=1
# alfabeto.split()
# dic = {}
# for i in alfabeto:
#     dic[i] = n
#     n+=1
# num=0
# for i in name:
#     num += dic[i]
# print(num)
#======================tentativa 2 usando menos linhas======================
nome = list(input("Nome Completo:").replace(" ","").upper())
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num=0
for i in nome:
    k = alfabeto.index(i)+1
    num+=k
print(num)