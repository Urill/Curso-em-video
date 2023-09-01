n = float(input('Digite o seu salário: '))
if n>1250.50:
    novoSal = n + (n * 0.10)
    print('Seu novo salário é de {:.2f}'.format(novoSal))
else:
    novoSal = n + (n * 0.15)
    print('Seu novo salário é de {:.2f}'.format(novoSal))