dic = {'A':1, 'B':2, 'C':3}
print(dic.keys())
print(dic.values())
print(dic.items())
print(len(dic))
print("Elementos no dicionário: ")
for letra in dic:
    print(letra)

print("Elementos específicos: ")
print(f"A: {dic['A']}")
print(f"B: {dic["B"]}")
print(f"C: {dic["C"]}")

for algaritmo, numero in dic.items():
    print(f"A letra {algaritmo} corresponde ao número {numero}")

print(list(range(3)))
print(list(range(2,20,2)))

nomes = ['João', 'Vitor', 'Luisa']
print(list(enumerate(nomes)))