"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
) # '10a' '10.5' '10' 

try: # Tentar executar o código dentro do try
    numero_float = float(numero_str) # Pode gerar um erro
    print('FLOAT:', numero_float) # Se não gerar erro, executa o print
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') # Se não gerar erro, executa o print
except: # Se der algum erro, executa o código dentro do except
    print('Isso não é um número') # Se der erro, executa esse print

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')