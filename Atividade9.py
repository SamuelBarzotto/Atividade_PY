# Faça um programa que leia o salário de um funcionário e o percentual de aumento, calcule
#e mostre o valor do aumento e o novo salário.
print("Informe um salário: ")
s= int(input())
print("Informe o percentual de aumento: ")
p= int(input())
a= s*(p/100)
ns= s+a
print("O aumento:", a, "e o novo salário:", ns)