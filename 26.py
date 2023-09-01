velo = float(input('Digite a velocidade: '))
limite = 80
if velo > limite:
    print('Vc foi multado')
    multa = (velo - limite) * 7
    print('Sua muta será de {} '.format(multa))
else:
    print('Pode continuar')