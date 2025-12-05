import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não esta disponivel no momento!')
else:
    print('COnsegui acessar o site pudim!')