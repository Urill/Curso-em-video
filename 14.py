ndias = float(input('Quantos dia vc rodou ? '))
nkm = float(input("Quanto km vc rodou ? "))
quantkm = nkm * 0.15
quantdias = ndias * 60
quantpag = quantdias + quantkm
print('O valor a pagar é {}'.format(quantpag))
