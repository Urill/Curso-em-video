total = [[],[]]
n = 0
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        total[0].append(n)
    if n % 2 == 1:
        total[1].append(n)
print(total)
print(sorted(total[0]))
print(sorted(total[1]))