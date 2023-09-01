from Ex104.lib.interface import *
def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<30}{dado[1]:>3}')

    finally:
        a.close()


def novocad(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora do novo cadastro')
        else:
            print('Novo cadastro adicionado')
            a.close()