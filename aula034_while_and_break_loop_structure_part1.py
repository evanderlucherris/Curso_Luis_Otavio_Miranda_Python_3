"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True # Loop infinito

while condicao: # Enquanto a condição for verdadeira
    nome = input('Qual o seu nome: ') # Pergunta o nome do usuário
    print(f'Seu nome é {nome}') # Imprime o nome do usuário

    if nome == 'sair': # Se o nome for 'sair'
        break # Interrompe o loop

print('Acabou') # Imprime 'Acabou' após o loop ser interrompido