valorcasa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
quantanos = int(input('Você irá pagar em quantos anos ? '))
prestacao = valorcasa / (quantanos * 12)
if prestacao > salario * 0.3:
    print('O empréstimo foi negado')
else:
    print('Empréstimo aprovado')
