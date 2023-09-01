media = 0
cont = 0
soma = 0
maior = menor = 0
print('Digite 1 para começar')
op = int(input('Digite a sua opção: '))
'''n = int(input('Digite um número: '))
op = str(input('Digite sim para continuar e Não para parar: ').strip().upper()[0])'''
while op == 1 or op in 'Ss':
    n = int(input('Digite um número: '))
    soma = soma + n
    cont += 1
    media = soma/cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            maior = n
    print('Digite Sim para continuar e Não para parar')
    op = str(input('Quer continuar ? ').strip().upper()[0])
print(media)
print(maior)
print(menor)
