# Faça um programa que leia 3 números e “diga” qual é o maior deles:
print("Digite um número: ")
nUM= int(input())
print("Digite o segundo número: ")
nDOIS= int(input())
print("Digite o último número: ")
nTRES= int(input())
if nUM>nDOIS and nUM>nTRES:
    print(nUM, "é o maior número.")
elif nDOIS>nUM and nDOIS>nTRES:
    print(nDOIS, "é o maior número.")
elif nTRES>nUM and nTRES>nDOIS:
    print(nTRES, "é o maior número.")