# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ') #string

if entrada == 'entrar': # condicional simples
    print('Você entrou no sistema') # bloco 1

    print(12341234) # bloco 1
elif entrada == 'sair': # condicional composta
    print('Você saiu do sistema') # bloco 2
else: # condicional completa
    print('Você não digitou nem entrar e nem sair.') # bloco 3

print('FORA DOS BLOCOS') # bloco 4 - fora dos blocos de código