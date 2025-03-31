# Faça programa que leia uma temperatura em graus Fahrenheit, calcular e escrever o valor
#correspondente em graus Celsius e Kelvin:
print("Informe uma temperatura em Fahrenheit: ")
f= int(input())
c= (f-32)/1.8
k= (f+459.67)/1.8
print("A temperatura em Celcius:", c, ", e em Kelvin:", k)