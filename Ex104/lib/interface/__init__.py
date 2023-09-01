def linha(tam=42):
    return '='*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('Erro. Digite um número válido')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida')
            return 0
        else:
            return n

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


