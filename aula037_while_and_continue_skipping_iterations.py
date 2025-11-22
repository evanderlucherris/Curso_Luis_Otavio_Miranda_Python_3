"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0 # Inicialização do contador

while contador <= 100: # Condição de parada
    contador += 1 # Atualização do contador

    if contador == 6: # Pula a iteração
        print('Não vou mostrar o 6.') # Mensagem opcional
        continue # Pula para a próxima iteração

    if contador >= 10 and contador <= 27: # Pula as iterações entre 10 e 27
        print('Não vou mostrar o', contador) # Mensagem opcional
        continue # Pula para a próxima iteração

    print(contador) # Mostra o valor do contador

    if contador == 40: # Encerra o loop quando o contador chegar a 40
        break # Encerra o loop


print('Acabou') # Mensagem final indicando o fim do loop