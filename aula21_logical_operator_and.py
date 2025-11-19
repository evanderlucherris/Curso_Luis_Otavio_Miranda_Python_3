# Operadores lógicos
# and (e) or (ou) not (não)
# and - Tidas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você já viu) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('Digite [E]ntrar ou [S]air: ') # E S
senha_digitada = input('Senha: ') # 123456
senha_permitida = '123456' # senha correta

if entrada == 'E' and senha_digitada == senha_permitida: # ambas as condições precisam ser verdadeiras
    print('Entrou no sistema') # acesso permitido
elif entrada == 'E' and senha_digitada != senha_permitida: # primeira condição verdadeira, segunda falsa
    print('Senha incorreta') # acesso negado
elif entrada == '': # nenhuma das condições verdadeiras
    print('Acesso negado, informe E ou S') # acesso negado
else: # segunda condição verdadeira
    print('Saiu do sistema') # acesso permitido

"""
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito com o operador and
"""
print(True and False and True) # Retorna False sempre que encontrar o primeiro False
print(True and 0 and True) # Retorna 0 sempre que encontrar o primeiro valor Falsy
print(True and 123 and 'Evander') # Retorna o último valor True