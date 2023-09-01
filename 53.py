contidade = 0
media = 0
nomevelho = ''
maioridadehomem = 0
quantmulher = 0
for c in range(1, 3):
    idade = int(input('Qual a idade da {} pessoa: '.format(c)))
    nome = str(input('Qual o nome da {} pessoa: '.format(c)))
    sexo = str(input('Qual o sexo da {} pessoa: '.format(c)))
    sexo = sexo.upper()
    contidade += idade
    if c == 1 and sexo == 'MASCUlINO' or sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'MASCULINO' or sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'FEMININO' or sexo in 'Ff' and idade < 20:
        quantmulher += 1

media = contidade / 4
print('A media de idade é {}'.format(media))
print('O mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Tem {} mulheres com menos de 20 anos'.format(quantmulher))

