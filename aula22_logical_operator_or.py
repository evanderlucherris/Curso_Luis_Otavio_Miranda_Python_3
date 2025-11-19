# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ') # E S
# senha_digitada = input('Senha: ') # 123456

# senha_permitida = '123456' # senha correta

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # true 
#     print('Entrar') # Entrar
# else: # false
#     print('Sair') # Sair

# Avaliação de curto circuito com or
# A variável recebe o primeiro valor verdadeiro encontrado
senha = input('Senha: ') or 'Sem senha' # ''  -> 'Sem senha'
print(senha) # Sem senha