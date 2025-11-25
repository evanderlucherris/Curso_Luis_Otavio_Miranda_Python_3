""" while/else """
string = 'Valor qualquer' # String sem espaço no final

i = 0 # Índice inicial
while i < len(string): # Enquanto o índice for menor que o tamanho da string
    letra = string[i] # Pega a letra na posição do índice

    if letra == ' ': # Se a letra for um espaço
        break # Sai do loop

    print(letra) # Imprime a letra
    i += 1 # Incrementa o índice
else: # Caso o loop termine normalmente (sem break)
    print('Não encontrei um espaço na string.') # Imprime mensagem
print('Fora do while.') # Imprime mensagem fora do loop