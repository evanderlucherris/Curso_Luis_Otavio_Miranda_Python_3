
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável 

# iteratador = iter(texto)  # iterator # cria o iterador

# while True: # loop infinito
#     try: # tenta executar o código
#         letra = next(iteratador) # pega o próximo valor
#         print(letra) # imprime o valor
#         break # sai do loop

for letra in texto: # iterável
    print(letra) # imprime cada letra
