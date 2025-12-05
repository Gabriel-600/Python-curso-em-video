'''num = int(input('Digite um numero:'))
for c in range (1, 11):                                                             + ou - certo 
    soma = num * c
    print(f'{num} x {c} = {soma}')'''



'''soma = cont = 0

num = int(input('Digite um numero para ver a tabuada: '))
while cont <10:
    if num <0:
        print('Encerrando...')
        break
    cont +=1
    soma = num * cont
    print(f'{num} x {cont} = {soma}')

print('Programa tabuada encerrado! ')'''




while True:
    num = int(input('Digite um numero: '))
    if num <0:
        break
    for c in range (1, 11):
        print (f'{num} x {c} = {num * c }')
    

print('Programa tabuada encerrado! ')
              