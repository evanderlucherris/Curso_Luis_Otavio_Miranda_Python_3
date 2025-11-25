# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python' # input('Digite um texto: ')

novo_texto = '' # string vazia para armazenar o novo texto
for letra in texto: # para cada letra na string texto
    novo_texto += f'*{letra}' # adiciona a letra com asterisco antes na nova string
    print(letra) # imprime a letra atual
print(novo_texto + '*') # imprime o novo texto com asterisco no final