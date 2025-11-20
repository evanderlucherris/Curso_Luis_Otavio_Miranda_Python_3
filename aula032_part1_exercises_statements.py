"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ') # pede ao usuário para digitar um número

try: # tenta converter a entrada para inteiro
    int_numero = int(numero) # converte a entrada para inteiro
    if int_numero % 2 == 0: # verifica se o número é par
        print(f'O número {int_numero} é par.') # informa que o número é par
    else: # se não for par, é ímpar
        print(f'O número {int_numero} é ímpar.') # informa que o número é ímpar
except ValueError: # se a conversão falhar, captura o erro
    print('Isso não é um número inteiro.') # informa que a entrada não é um número inteiro