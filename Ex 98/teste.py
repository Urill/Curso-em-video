import moeda
p = float(input('Digite o preco: '))
tax = float(input('Digite a taxa: '))

print(moeda.dobro(p))
print(moeda.metade(p))
print(moeda.aumentar(p, tax))
print(moeda.diminuir(p, tax))