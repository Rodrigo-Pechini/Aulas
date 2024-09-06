import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('Este site não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    print(site.read())

