# Fazer o jogo Jokenpô:
print("Escolha sua opção P1- pe, pa, te: ")
pUM= str(input())
print("Escolha sua opção P2- pe, pa, te: ")
pDOIS= str(input())
if pUM=="pe" and pDOIS=="pe":
    print("Deu empate.")
elif pUM=="pe" and pDOIS=="pa":
    print("Jogador 2 ganhou.")
elif pUM=="pe" and pDOIS=="te":
    print("Jogador 1 ganhou.")
elif pUM=="pa" and pDOIS=="pe":
    print("Jogador 1 ganhou.")
elif pUM=="pa" and pDOIS=="pa":
    print("Deu empate.")
elif pUM=="pa" and pDOIS=="te":
    print("Jogador 2 ganhou.")
elif pUM=="te" and pDOIS=="pe":
    print("Jogador 2 ganhou.")
elif pUM=="te" and pDOIS=="pa":
    print("Jogador 1 ganhou.")
elif pUM=="te" and pDOIS=="te":
    print("Deu empate.")