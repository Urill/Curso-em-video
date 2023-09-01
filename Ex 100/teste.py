import moeda
from moeda import moeda as form
p = float(input('Digite o preco: '))
tax = float(input('Digite a taxa: '))

print(f'A metade de {form(p)} é {form(moeda.metade(p))}')
print(f'O dobro de {form(p)} é {form(moeda.dobro(p))}')
print(f'Aumentnado {tax}% de {form(p)} temos {form(moeda.aumentar(p, tax))}')
print(f'Diminuindo {tax}% de {form(p)} temos {form(moeda.diminuir(p, tax))}')
