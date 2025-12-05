r1 = float (input('Digite o comprimento da reta 1: '))
r2 = float (input ('DIgite o comprimento da reta 2: '))
r3 = float (input('Digite o comprimento da reta3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ('É possivel fazer um triangulo! ')

else:
    print ('Não é possivel fazer um triangulo! ') 