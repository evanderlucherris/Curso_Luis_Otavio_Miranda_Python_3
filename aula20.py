#EXERCÍCIO DE PROGRAMAÇÃO COM IF E COMPARAÇÃO

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor = {primeiro_valor} é MAIOR que o segundo valor = {segundo_valor}")
elif segundo_valor > primeiro_valor:
    print(f"O segundo valor = {segundo_valor} é MAIOR que o primeiro valor = {primeiro_valor}")
elif primeiro_valor == segundo_valor:
    print(f"O primeiro valor {primeiro_valor} é IGUAL ao segundo valor {segundo_valor}")

    """
    PODERIA SER FEITODE FORMA MAIS SIMPLES:
    
    primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
    """