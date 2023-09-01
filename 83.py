aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = int(input('Digite a média: '))
'''   op = str(input('Quer continuar ? S/N: ')).strip()[0]
    situação.append(aluno.copy())
    while op not in 'SsNn':
        print('Opção inválida, tente novamente')
        op = str(input('Quer continuar ? S/N: ')).strip()[0]
if op in 'Nn':
        break'''
if aluno['media'] < 6:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] >= 6:
    aluno['situação'] = 'Aprovado'
print(aluno)
