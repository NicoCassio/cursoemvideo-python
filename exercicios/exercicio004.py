v = input('Digite algo: ')
print('Tipo: {}'.format(type(v)))
print('Só espaços: {}'.format(v.isspace()))
print('É número: {}'.format(v.isnumeric()))
print('É palavra: {}'.format(v.isalpha()))
print('É alfanumérico: {}'.format(v.isalnum()))
print('Maiúscula: {}'.format(v.isupper()))
print('Minúscula: {}'.format(v.islower()))
