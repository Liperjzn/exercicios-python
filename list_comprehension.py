tabuada = [1,2,3,4,5,6,7,8,9,10]
calculo = [numero*10 for numero in tabuada]
print(calculo)

calculo.append(110)
print(calculo)

calculo.remove(10)
print(calculo)

calculo.insert(0, 10)
print(calculo)

soma = sum(calculo)
print(soma)

calculo.clear()
print(calculo)

lista2 = [i for i in range(1,100) if i%2==0]
print(lista2)