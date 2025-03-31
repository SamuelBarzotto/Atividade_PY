# Faça um programa que leia a idade de um nadador e classifique-o numa das seguintes categorias:
#Idoso (idade >= 65), Adulto (idade >= 21), Juvenil (idade >= 14), Infantil (idade >=9) e
#Mirim (Idade < 9):
print("Informe a idade do nadador: ")
i= int(input())
if i>=65:
    print("Categoria Idoso.")
elif i>=2:
    print("Categoria Adulto.")
elif i>=14:
    print("Categoria Juvenil.")
elif i>=9:
    print("Catgoria Infantil.")
elif i<9:
    print("Categoria Mirim.")