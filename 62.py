import random
vit = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = random.randint(0,10)
    total = computador + jogador
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} o computador jogou {computador} o total foi {total}', end=' ')
    print('Deu par' if total % 2 ==0 else 'Deu impar')
    if op == 'P':
        if total % 2 == 0:
            print('Vc ganhou')
            vit += 1
        else:
            print('Vc perdeu')
            break
    elif op == 'I':
        if total % 2 == 1:
            print('Vc ganhou')
            vit += 1
        else:
            print('Vc perdeu')
            break
    print('Tente novamente')
print(f'Vc venceu {vit}')

