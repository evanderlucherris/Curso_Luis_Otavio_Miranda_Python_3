"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora atual (0-23): ')

try:
    int_hora = int(hora)
    if 0 <= int_hora <= 11:
        print('Bom dia!')
    elif 12 <= int_hora <= 17:
        print('Boa tarde!')
    elif 18 <= int_hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida. Por favor, digite um número entre 0 e 23.')
except ValueError:
    print('Isso não é um número inteiro.')