"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora atual (0-23): ') # Solicita a hora ao usuário

try: # Tenta converter a entrada para inteiro
    int_hora = int(hora) # Converte a entrada para inteiro
    if 0 <= int_hora <= 11: # Verifica o intervalo da hora
        print('Bom dia!') # Saudação para manhã 
    elif 12 <= int_hora <= 17: # Verifica o intervalo da hora
        print('Boa tarde!') # Saudação para tarde
    elif 18 <= int_hora <= 23: # Verifica o intervalo da hora
        print('Boa noite!') # Saudação para noite
    else: 
        print('Hora inválida. Por favor, digite um número entre 0 e 23.') # Mensagem para hora inválida
except ValueError: # Captura erro de conversão
    print('Isso não é um número inteiro.') # Mensagem para entrada inválida