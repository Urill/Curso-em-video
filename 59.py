cont = 0
soma = 0
n = int(input('Digite um número: '))
#print('Se vc quiser parar digite 999')
while n != 999:
    print('Se vc quiser parar digite 999')
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
print(f'A quantdade de números digitados é: {cont}')
print(f'A soma dos números é: {soma}')
