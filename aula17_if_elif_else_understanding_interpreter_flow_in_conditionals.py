# if / elif      / else
# se / se não se / se não

condicao1 = True #verdadeiro
condicao2 = True #verdadeiro
condicao3 = True #verdadeiro
condicao4 = True #verdadeiro

if condicao1: # condicional simples
    print('Código para condição 1') # bloco 1
    print('Código para condição 1') # bloco 1
elif condicao2: # condicional composta
    print('Código para condição 2') # bloco 2
elif condicao3: # condicional completa
    print('Código para condição 3')
elif condicao4: # condicional completa
    print('Código para condição 4') # bloco 3
else: # condicional completa
    print('Nenhuma condição foi satisfeita.') # bloco 4

if 10 == 10: # condicional simples
    print('Outro if') # bloco 5

print('Fora do if') # bloco 6 - fora dos blocos de código