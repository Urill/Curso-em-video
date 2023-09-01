import urllib.request
import urllib

try:
    site = urllib.request.urlopen('https://www.instagram.com')
except urllib.error.URLError:
    print('Erro')
else:
    print('Funcionando')
