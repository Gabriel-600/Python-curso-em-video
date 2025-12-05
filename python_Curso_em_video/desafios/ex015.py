km = float (input('Digite quantos km rodados '))
d = int (input('Digite quantos dias ficou com ele '))

roda = km * 0.15
dias = d * 60
total = roda + dias

print ('Voce ficou com ele {} dias então esta devendo {:.2f}'.format (d, dias),end=' ')
print ('Voce rodou {}km, então esta devendo {}'.format(km, roda))

print ('o valor total é {}'.format (total))