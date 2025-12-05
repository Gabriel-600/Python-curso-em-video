print ('='*20)
print ('10 TERMOS DE UMA PA')
print ('='*20)
num1 = int (input('Primeiro termo:'))
razao = int (input('Razão: '))
decimo = num1 + (10 - 1) * razao



for c in range (num1, decimo + razao, razao):
    print ('{}'.format(c), end='-')


print ('Acabou!')