frase = 'aaaooo' # input('Digite uma frase: ')

i = 0 # índice para percorrer a string
qtd_apareceu_mais_vezes = 0 # quantidade da letra que apareceu mais vezes
letra_apareceu_mais_vezes = '' # letra que apareceu mais vezes

while i < len(frase): # enquanto o índice for menor que o tamanho da string
    letra_atual = frase[i] # letra na posição do índice

    if letra_atual == ' ': # se a letra for um espaço, pula para a próxima iteração
        i += 1 # incrementa o índice
        continue # pula para a próxima iteração

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual) # conta quantas vezes a letra atual apareceu na frase

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual: # se a quantidade da letra que apareceu mais vezes for menor que a quantidade da letra atual
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual # atualiza a quantidade da letra que apareceu mais vezes
        letra_apareceu_mais_vezes = letra_atual # atualiza a letra que apareceu mais vezes

    i += 1 # incrementa o índice

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
) # imprime o resultado