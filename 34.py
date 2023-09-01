num = int(input('Digite um número inteiro: '))
print('Escolha 1 para conversão binária, 2 para conversão octal e 3 para conversão hexadecimal')
op = int(input('Sua opção: '))
if op == 1:
    print('O número convertido para binário é {}'.format(bin(num)[2:]))
elif op == 2:
    print('O número convertido para octal é {}'.format(oct(num)[2:]))
elif op == 3:
    print('O número convertido para hexadecimal é {}'.format(hex(num)[2:]))
