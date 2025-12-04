for i in range(10): # de 0 a 9
    if i == 2: # quando i for 2
        print('i é 2, pulando...')
        continue # pula o restante do código e volta para o for

    if i == 8: # quando i for 8 
        print('i é 8, seu else não executará')
        break # sai do loop

    for j in range(1, 3): # de 1 a 2
        print(i, j) # imprime i e j
else: # só executa se o for NÃO tiver sido interrompido pelo break
    print('For completo com sucesso!') # imprime mensagem