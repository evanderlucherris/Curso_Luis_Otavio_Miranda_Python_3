# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

# senha = input('Senha: ')
# print(not True)  # False
# print(not False)  # True

entrada = input('[E]ntrar [S]air: ') # Pede para o usuário entrar ou sair
senha_digitada = input('Senha: ') # Pede para o usuário digitar a senha

senha_permitida = '123456' # Senha correta

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # Verifica se a entrada é "E" ou "e" e se a senha está correta
    print('Entrar') # Permite a entrada
elif not entrada: # Verifica se a entrada está vazia
    print('Inválido, digite "E" oi "e"') # Mensagem de erro
elif not senha_digitada: # Verifica se a senha está vazia
    print('Você não digitou a senha') # Mensagem de erro
elif entrada == 'S' or 's': # Verifica se a entrada é "S" ou "s"
    print('Sair') # Permite sair