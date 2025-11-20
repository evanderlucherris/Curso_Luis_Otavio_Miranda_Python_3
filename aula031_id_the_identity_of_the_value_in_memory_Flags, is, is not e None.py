"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False # altere para True ou False para testar
passou_no_if = None # Flag inicializada com None

if condicao: 
    passou_no_if = True # Marca a flag como True
    print('Faça algo') # Se a condição for verdadeira
else:
    print('Não faça algo') # Se a condição for falsa

if passou_no_if is None: # Verifica se a flag é None
    print('Não passou no if') # Se a flag for None
else:
    print('Passou no if') # Se a flag não for None