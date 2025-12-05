from datetime import date
atual = date.today().year
totalme = 0
totalmai = 0
for c in range (1, 8):
    nasc = int(input('Digite a {}º data de aniversario: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        totalmai += 1
    else:
        totalmai +=1
print ('Tivemos {} maiores de idade!'.format(totalmai))
print ('Tivemos {} menores de idade!'.format(totalme))