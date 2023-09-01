from Ex104.lib.interface import *
from Ex104.lib.Arquivo import *
from time import sleep

arq = 'CursoemVídeo.txt'
if not arqexiste(arq):
    criararq(arq)
while True:
    resp = menu(['Pessoas cadastradas', 'Novo cadastro', 'Sair do sistema'])
    if resp == 1:
        lerarq(arq)
    elif resp == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        novocad(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('Digite uma opção válida')
    sleep(1)

