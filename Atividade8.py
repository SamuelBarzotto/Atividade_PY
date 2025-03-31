# Faça programa que leia uma temperatura em graus Celsius, calcular e escrever o valor
#correspondente em graus Fahrenheit e Kelvin.
print("Informe uma temperatura em Celcius: ")
c= int(input())
k= c+273.15
f= (c*1.8)+32
print("A temperatura em Kelvin:", k, ", e em Fahrenheit:", f)