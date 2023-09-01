num = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez'
while True:
    n = int(input('Digite um número: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente.')
print(f'Você digitou o número {num[n]}')