# Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o valor
#da compra for menor que 20,00; caso contrário, o lucro será de 30%. Ler o valor
#do produto e imprimir o valor da venda, conforme as taxas do enunciado:
print("Digite o valor do produto: ")
v= int(input())
if v<20:
    vaUM= (v*0.45)+v
    print("O valor com lucro de 45% é:", vaUM)
elif v>=20:
    vaDOIS= (v*0.3)+v
    print("O valor com lucro de 30% é:", vaDOIS)