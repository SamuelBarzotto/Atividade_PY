# Faça um programa que converta a temperatura. Deve ser selecionada a
#temperatura que será inserida assim como a que será exibida. As temperaturas
#utilizadas devem ser Celsius, Fahrenheit e Kelvin:
print("Digite o tipo da temperatura (k, f, c): ")
t= str(input())
print("Digite o valor da temperatura: ")
v= int(input())
print("Digite o tipo de temperatura para converter (k, f, c): ")
c= str(input())
if t=="k" and c=="f":
    conversao= (v*1.8)-459.67
    print(v, "K° é:", conversao, "F°.")
elif t=="k" and c=="c":
    conversao= v-273.15
    print(v, "K° é:", conversao, "C°")
elif t=="f" and c=="k":
    conversao= (v+459.67)/1.8
    print(v, "F° é:", conversao, "K°")
elif t=="f" and c=="c":
    conversao= (v-32)/1.8
    print(v, "F° é:", conversao, "C°")
elif t=="c" and c=="k":
    conversao= v+273.15
    print(v, "C° é:", conversao, "K°")
elif t=="c" and c=="f":
    conversao= (v*1.8)+32
    print(v, "C° é:", conversao, "F°")