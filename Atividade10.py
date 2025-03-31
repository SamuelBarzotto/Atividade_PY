# Faça um programa que leia um número, verifique se este número é positivo ou negativo.
#Se for negativo mostre a mensagem "Você digitou um numero negativo", Senão mostre:
#"Você digitou um número positivo.

# Faça um programa que leia um número, verifique se este número é positivo, negative ou Zero.
#Se for negativo mostre a mensagem "Você digitou um numero negativo", Se for positivo
#mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou zero”.
print("Digite um número positivo ou negativo: ")
n= int(input())
if n<0:
    print("Você digitou um número negativo.")
elif n>0:
    print("Você digitou um número positivo.")
elif n==0:
    print("Você digitou 0.")