"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] -> início:fim:passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo' # 9 caracteres (índices 0 a 8)
print(len(variavel)) # 9
print(len('Olá mundo'[3])) # 1
print(variavel[0:12:1]) # Olá mundo
print(variavel[-9:]) # Olá mundo
print(variavel[:10:1]) # Olá mundo
print(variavel[:10:2]) # Oámdo
print(variavel[::-1]) # odnum álO
print(variavel[-1:-10:-1]) # odnum álO
print(variavel[-1:-10:-2]) # o uá