"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ') # Solicita o nome ao usuário
tamanho_nome = len(nome) # Calcula o tamanho do nome

if tamanho_nome > 1: # Verifica se o nome tem mais de uma letra
    if tamanho_nome <= 4: # Verifica se o nome tem 4 letras ou menos
        print('Seu nome é curto.') # Mensagem para nome curto
    elif 5 <= tamanho_nome <= 6: # Verifica se o nome tem entre 5 e 6 letras
        print('Seu nome é normal.') # Mensagem para nome normal
    else: # Caso o nome tenha mais de 6 letras
        print('Seu nome é muito grande.') # Mensagem para nome muito grande
else: # Caso o nome tenha 1 letra ou menos
    print('Digite mais de uma letra.') # Mensagem para nome inválido