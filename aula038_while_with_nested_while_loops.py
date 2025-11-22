"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5 # Número de linhas
qtd_colunas = 5 # Número de colunas

linha = 1 # Inicialização da linha
while linha <= qtd_linhas: # Condição de parada da linha
    coluna = 1 # Inicialização da coluna
    while coluna <= qtd_colunas: # Condição de parada da coluna
        print(f'{linha=} {coluna=}') # Mostra a linha e a coluna
        coluna += 1 # Atualização da coluna
    linha += 1 # Atualização da linha


print('Acabou') # Mensagem final indicando o fim do loop