preco = float(input('Digite o valor do produto: '))
print('Escolha a opção de pagagmento. '
      '\nPara pagamento à vista, dinheiro ou cheque: [1]'
      '\nPara pagamento à vista, cartão: [2]'
      '\nPara em até 2x no cartão: [3]'
      '\nPara 3x ou mais no cartão: [4]')
op = int(input('Sua opção: '))
if op == 1:
    valorpag = preco - (preco * 0.10)
    print('O valor a ser pago é R${}'.format(valorpag))
elif op == 2:
    valorpag = preco - (preco * 0.05)
    print('O valor a ser pago é R${}'.format(valorpag))
elif op == 3:
    valorpag = preco
    print('O valor a ser pago é R${}'.format(valorpag))
elif op == 4:
    valorpag = preco + (preco * 0.20)
    print('O valor a ser pago é R${}'.format(valorpag))
else:
    print('Opção inválida')
