print("A meta desejada é de 100 voluntários")
voluntarios = int(input("Digite o número de vonlutários: "))
if voluntarios < 25:
    print("O número de voluntários está abaixo dos 25 porcento da meta")
elif(voluntarios > 25 and voluntarios < 50):
    print("O número de voluntários está acima de 25 porcento, mas abaixo da metade da meta")
elif(voluntarios > 50 and voluntarios < 75):
    print("O número de voluntários está acima da metade, mas abaixo de 75 porcento da meta")
elif(voluntarios > 75 and voluntarios < 100):
    print("O número de voluntários está acima de 75 porcento, mas abaixo do valor mínimo da meta")
elif(voluntarios >=100):
    print("A meta foi atingida")