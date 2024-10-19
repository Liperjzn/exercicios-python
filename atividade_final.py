Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def venda_de_produtos():
...     try:
...         nome_produto = input("Escreva o nome do produto: ") 
...         preço = float(input('Escreva o preço: ')
...         quantidade = int(input('Escreva a quantidade: ')
...     except TypeError as erro:
...         print("Os campos 'quantidade e 'preço' devem conter apenas valores numéricos, tente novamente!")
...     valor_total = preço*quantidade
...     print(valor_total)
...     
...     try:
...         metodo_pagamento = int
...         metodo_pagamento = input("Insira o método de pagamento (1-DINHEIRO/2-PIX/3-CARTÃO (DÉBITO/CRÉDITO)-5)")
...         if metodo_pagamento > 5 or metodo_pagamento <= 0:
...             print('Método de pagamento inválido! Tente novamente')
...         else:
...             print('Muito obrigado, volte sempre!')
...     except TypeError as erro:
...         print("O campo 'metodo_pagamento' deve conter apenas valores numéricos, tente novamente!")
