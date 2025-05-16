# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
# print(not True)  # False
# print(not False)  # True

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
elif not entrada:
    print('Inválido, digite "E" oi "e"')
elif not senha_digitada:
    print('Você não digitou a senha')
elif entrada == 'S' or 's':
    print('Sair')