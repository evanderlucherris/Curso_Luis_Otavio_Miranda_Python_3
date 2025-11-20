# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# E v a n d e r
#-7-6-5-4-3-2-1

# nome = 'Evander'
# print(nome[2])
# print(nome[-4])
# print('der' in nome)
# print('van' in nome)
# print(10 * '-')
# print('eva' not in nome)
# print('nder' not in nome)

nome = input('Digite o seu nome: ') # Pede para o usuário digitar o nome
encontrar = input('Digite o que deseja encontrar: ') # Pede para o usuário digitar o que deseja encontrar

if encontrar in nome: # Verifica se o que o usuário digitou está no nome
    print(f'{encontrar} está em {nome}') # Mensagem de confirmação
else: # Verifica se o que o usuário digitou não está no nome
    print(f'{encontrar} não está em {nome}') # Mensagem de negação