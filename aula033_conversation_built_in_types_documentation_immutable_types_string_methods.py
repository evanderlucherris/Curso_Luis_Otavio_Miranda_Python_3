"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = '1000'                                       # string é imutável
# outra_variavel = f'{string[:3]}ABC{string[4:]}'     # f-string também cria uma nova string
# print(string)                                       # Imprime a string original
# print(outra_variavel)                               # Imprime a nova string
print(string.zfill(10))                               # Preenche com zeros à esquerda até o tamanho 10