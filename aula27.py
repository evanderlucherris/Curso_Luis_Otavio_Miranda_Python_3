"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[0:10:1])
print(variavel[:10:1])
print(variavel[:10:2])
print(variavel[::-1])
print(variavel[-1:-10:-1])
print(variavel[-1:-10:-2])