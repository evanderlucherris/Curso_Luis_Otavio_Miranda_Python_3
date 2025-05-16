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

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')