"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a -> repr, str, ascii.
"""
variavel = 'ABC' # String
print(f'{variavel}') # Simples
print(f'{variavel: >10}') # Direita
print(f'{variavel: <10}.') # Esquerda
print(f'{variavel: ^10}.') # Centro
print(f'{1000.4873648123746:0=+10,.1f}') # Força o número a aparecer antes dos zeros
print(f'O hexadecimal de 1500 é {1500:08X}') # Hexadecimal
print(f'{variavel!r}') # Usando repr()