nome = input('Digite seu nome completo: ').strip ()
div = nome.split()
#maiusculo
print (nome.upper())

#minusculo
print (nome.lower())                                           #conseguiiiiiiiiiiii

#contar letras sem contar os espaços
print (len(nome) -  nome.count (' '))

#quantas letras tem o primeiro nome
print (len(div [0]))

#ou     print ('seu primeiro nome tem {} letras'.format(nome.find(' ')) )