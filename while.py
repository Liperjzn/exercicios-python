fimDoLoop = 0
while True:
    int(input("Digite um número: "))
    encerrarLoop = int(input("Deseja sair do programa? (1-SIM/0-NÃO) "))
    fimDoLoop = encerrarLoop
    if fimDoLoop == 1:
        break
print("Fim do programa")
