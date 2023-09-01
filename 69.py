n = (int(input('Digite um número:')),int(input('Digite um número:')),int(input('Digite um número:')),int(input('Digite um número:')))
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}')
print('Os números pares foram:')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
