sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Digite o seu sexo novamente: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'MASCULINO'
if sexo == 'F':
    sexo = 'FEMININO'
print('Sexo {} registrado'.format(sexo))
