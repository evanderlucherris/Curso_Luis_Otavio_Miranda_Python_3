""" Calculadora com while """

while True: # Loop principal da calculadora
    numero_1 = input('Digite um número: ') # Primeiro número
    numero_2 = input('Digite outro número: ') # Segundo número
    operador = input('Digite o operador (+-*/): ') # Operador
    
    numeros_validos = None # Variável de controle
    numero_1_float = 0 # Primeiro número convertido
    numero_2_float = 0 # Segundo número convertido

    try: # Tenta converter os números para float
        numero_1_float = float(numero_1) # Primeiro número convertido
        numero_2_float = float(numero_2) # Segundo número convertido
        numeros_validos = True # Números são válidos
    except: # Se der erro na conversão
        numeros_validos = None # Números inválidos

    if numeros_validos is None: # Verifica se os números são válidos
        print('Um ou ambos os números digitados são inválidos.') # Mensagem de erro
        continue # Reinicia o loop

    operadores_permitidos = '+-*/' # Operadores permitidos

    if operador not in operadores_permitidos: # Verifica se o operador é válido
        print('Operador inválido.') # Mensagem de erro
        continue # Reinicia o loop

    if len(operador) > 1: # Verifica se o operador tem mais de um caractere
        print('Digite apenas um operador.') # Mensagem de erro
        continue # Reinicia o loop
    
    print('Realizando sua conta. Confira o resultado abaixo.') # Mensagem de processamento
    if operador == '+': # Verifica se o operador é soma
        print(f'{numero_1_float}+{numero_2_float}=', numero_1_float + numero_2_float) # Mostra o resultado da soma
    if operador == '-': # Verifica se o operador é subtração
        print(f'{numero_1_float}-{numero_2_float}=', numero_1_float - numero_2_float) # Mostra o resultado da subtração
    if operador == '/': # Verifica se o operador é divisão
        print(f'{numero_1_float}/{numero_2_float}=', numero_1_float / numero_2_float) # Mostra o resultado da divisão
    if operador == '*': # Verifica se o operador é multiplicação
        print(f'{numero_1_float}*{numero_2_float}=', numero_1_float * numero_2_float) # Mostra o resultado da multiplicação
    else: # Nunca deveria chegar aqui
        print('Nunca deveria chegar aqui.') # Mensagem de erro inesperado


    sair = input('Deseja sair? (s/n): ').lower().startswith('s') # Pergunta para sair
    
    if sair is True: # Verifica se o usuário quer sair
        break # Sai do loop