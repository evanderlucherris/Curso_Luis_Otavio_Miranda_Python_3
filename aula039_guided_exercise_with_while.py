"""
Iterando strings com while
"""

nome = 'Evander' # Nome para iteração
tamanho_nome = len(nome) # Tamanho do nome
indice = 0 # Índice inicial

while indice < tamanho_nome: # Condição de parada
    print(nome[indice], end='') # Mostra o caractere na posição do índice

    if indice < tamanho_nome - 1: # Verifica se não é o último caractere
        print('*', end='') # Mostra o separador

    indice += 1 # Atualiza o índice