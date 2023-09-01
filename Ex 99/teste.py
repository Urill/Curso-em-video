import moeda
p = float(input('Digite o preco: '))
tax = float(input('Digite a taxa: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentnado {tax}% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, tax))}')
print(f'Diminuindo {tax}% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, tax))}')