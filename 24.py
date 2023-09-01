n = str(input('Digite a frase: ')).upper()

print('A letra a aparece {} vezes'.format(n.count('A')))
print('A primeira letra A aparece na posição {}'.format(n.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(n.rfind('A')+1))
