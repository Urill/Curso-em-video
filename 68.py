from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for c in n:
    print(c, end='')
print(f'\n{n}')
print(f'{max(n)}')
print(f'{min(n)}')