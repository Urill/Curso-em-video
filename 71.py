"""valor = list()
n = int(input('Digite a quantidade de valores: '))
for c in range(0, n):
    valor.append(int(input('Digite os valores: ')))
for c, v in enumerate(valor):
    print(f'os valores são {v} e estão na posição {c}')"""

valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Vc digitou os calores {valores}')
print(f'O maior valor foi {max(valores)} e estava na posição {valores.index(max(valores))+1}')
print(f'O menor valor foi {min(valores)} e estava na posição {valores.index(min(valores))+1}')
