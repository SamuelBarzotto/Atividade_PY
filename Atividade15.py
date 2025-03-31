# Faça um programa que leia dois números e efetua a adição. Se o valor somado for maior
#que 20, este deverá ser apresentado somando-se a ele 8, se o valor somado for menor
#ou igual a 20, este deverá ser apresentado subtraindo-se 5:
print("Digite um numero: ")
nUM= int(input())
print("Digite outro numero: ")
nDOIS= int(input())
a= nUM+nDOIS
if a>20:
    a= a+8
    print("A soma deles adicionada de 8 e:", a)
elif a<=20:
    print("A soma deles subtraída de 5 e:", a)