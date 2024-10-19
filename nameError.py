try:
    print(valor)
except NameError as tratarErro1:
    print("Erro, contate o administrador")

try:
    valor1 = 10
    valor2 = 'vinte'
    soma = valor1 + valor2
except TypeError as erro:
    print("Você só pode calcular valores do tipo número")

try:
    matricula,curso,periodo = [2023,'Python']
except ValueError as erro:
    print("Você esqueceu de passar um parâmetro")

try:
    alunos = ['Maria','João','Pedro']
    print(alunos[3])
except IndexError as erro:
    print("índice inexistente")

def dividir():
    try:
        num1 = input("Digite um número inteiro: ")
        num2 = input("Digite outro número inteiro: ")
        divisao = int(num1)/int(num2)
        print("Resultado da divisão:", divisao)
    except ZeroDivisionError as erro:
        print("Você não pode dividir por 0")

try:
    letras = {'A':1, 'B':2, 'C':3}
    print(letras['D'])
except KeyError as erro:
    print("Chave inválida")

   