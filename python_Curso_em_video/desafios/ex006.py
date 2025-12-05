num = int (input('Digite um numero '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print (' O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format (num, dobro, triplo, raiz))

#outra forma:   

n = int (input('Digite um numero '))
print ('o dobre de {} vale {}'.format (n, (n*2)))
print ('o triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format (n, (n*3, n, (n**(1/2)))))