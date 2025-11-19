"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Evander' # String
preco = 1000.95897643 # Float
variavel = '%s, o preço é R$%.2f' %(nome, preco) # Formatação com 2 casas decimais
print(variavel) # Evander, o preço é R$1000.96
print('O hexadecimal de %d é %08X' % (1500,1500)) # O hexadecimal de 1500 é 000005DC

# POSSO ESCOLHER ENTRE 3 OPÇÕES DE FORMATAÇÃO
# SENDO O METODO .FORMAT() OU F-STRINGS (PYTHON 3.6+) OU A INTERPOLAÇÃO COM % (ANTIGA)