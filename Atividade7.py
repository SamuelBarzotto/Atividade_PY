# Faça programa que leia uma temperatura em graus Kelvin, calcular e escrever o valor
#correspondente em graus Fahrenheit e Celsius:
print("Informe uma temperatura em Kelvin: ")
k= int(input())
c= k-273.15
f= (k*1.8)-459.67
print("A temperatura em Celcius:", c, ", e em Fahrenheit:", f)