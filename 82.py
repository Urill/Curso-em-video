ficha = list()
while True:
    nome = str(input('Digite o nome: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    ficha.append([nome, [n1, n2], media])
    op = str(input('Quer continuar ? [S/N]: ')).strip()[0]
    while op not in 'SsNn':
        print('Opção inválida, tente novamente')
        op = str(input('Quer continuar ? [S/N]: ')).strip()[0]
    if op in 'Nn':
        break

print('-='*30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>9}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostra as notas de qual aluno ? (999 para interromper) '))
    if opc == 999:
        print('Fim')
        break
    if opc >len(ficha)-1:
        break
    if opc <= len(ficha)-1:
        print(f'Notas do aluno {ficha[opc][0]} são {ficha[opc][1]}')

