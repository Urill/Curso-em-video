import datetime
n= int(input('Digite o ano ou coloque 0 para o ano atual: '))
#if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 :
#    print('O ano é bissexto')
#else:
#    print('O ano não é bissexto')
if n == 0:
    n = datetime.date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 :
    print('O ano atual é bissexto')
else:
   print('O ano atual não é bissexto')