frase = str(input('qual é o palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é palíndromo')
