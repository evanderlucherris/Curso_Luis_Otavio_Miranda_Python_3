# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) # converte str para int
print(type(float('1') + 1)) # converte str para float e faz a soma
print(bool(' ')) # str não vazia é True
print(str(11) + 'b') # converte int para str e faz a concatenação