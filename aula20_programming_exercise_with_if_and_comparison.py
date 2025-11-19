#EXERCÍCIO DE PROGRAMAÇÃO COM IF E COMPARAÇÃO

primeiro_valor = input('Digite o peirmeiro valor: ') #string
segundo_valor = input('Digite o segundo valor: ') #string

if primeiro_valor >= segundo_valor: # comparação entre strings
    print(
        f'O primeiro valor {primeiro_valor}, '
        f'é maior ou igual ao segundo valor {segundo_valor}.'
        ) #bloco do if
else: # bloco do else
    print(
        f'O segundo valor {segundo_valor}, '
        f'é maior que o primeiro valor {primeiro_valor}.'
        ) #bloco do else
