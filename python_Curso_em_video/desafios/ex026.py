frase = str(input('Digite uma frase: ')).upper().strip()
print ('A letra A aparece na posição {} da frase'.format(frase.find('A')+1))
print ('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print ('A ultima letra A apareceu na posiçao {} da frase'.format(frase.rfind('A')+1))

