a = 'AAAAA' #string
b = 'BBBBBB' #string
c = 1.1 #float
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' # string com o método format
formato = string.format(
    nome1=a, nome2=b, nome3=c
) # string formatada com o método format

print(formato) # b=BBBBBB a=AAAAA a=AAAAA c=1.10