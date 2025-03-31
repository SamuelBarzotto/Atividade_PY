# Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas,
#se a media aritmética for: Media maior ou igual a 7 – ALUNO APROVADO;
#Media maior ou igual a 5 e menor que 7 – ALUNO EM RECUPERAÇÃO;
#Media menor que 5 – ALUNO REPROVADO:
print("Digite uma nota: ")
nUM= int(input())
print("Digite a segunda nota: ")
nDOIS= int(input())
print("Digite a terceira nota: ")
nTRES= int(input())
media= (nUM+nDOIS+nTRES)/3
if media>=70:
    print("Aluno aprovado.")
elif media>=50 and media<70:
    print("Aluno em recuperação.")
elif media<50:
    print("Aluno reprovado.")