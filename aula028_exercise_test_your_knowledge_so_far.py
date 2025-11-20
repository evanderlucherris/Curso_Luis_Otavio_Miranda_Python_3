"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ') # Peça ao usuário para digitar seu nome
idade = input('Digite a sua idade: ') # Peça ao usuário para digitar sua idade

if nome and idade: # Se nome e idade forem digitados:
    print(f'Seu nome é {nome}') # Exiba: Seu nome é {nome}
    print(f'Seu nome invertido é {nome[::-1]}') # Exiba: Seu nome invertido é {nome invertido}
    if ' ' in nome: # Verifica se há espaços no nome
        print('Seu nome contém espaços') # Exiba: Seu nome contém (ou não) espaços
    else:
        print('Seu nome não contém espaços') # Exiba: Seu nome contém (ou não) espaços
    print(f'Seu nome tem {len(nome)} letras') # Exiba: Seu nome tem {n} letras
    print(f'A primeira letra do seu nome é {nome[0]}') # Exiba: A primeira letra do seu nome é {letra}
    print(f'A última letra do seu nome é {nome[-1]}') # Exiba: A última letra do seu nome é {letra}
else:
    print('Desculpe, você deixou campos vazios.') # Se nada for digitado em nome ou idade: exiba "Desculpe, você deixou campos vazios."