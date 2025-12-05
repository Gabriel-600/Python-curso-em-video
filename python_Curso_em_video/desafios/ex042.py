r1 = float (input('Digite o Comprimento da reta 1: '))
r2 = float (input('Digite o comprimento da reta 2: '))
r3 = float (input('Digite o comprimento da reta 3: '))


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:

 if r1 == r2 and r2 == r3:
    print ('Equilatero! lados iguais!')

 elif r1 == r2 or r1 == r3 or r2 == r3:
    print ('Isósceles! 2 lados iguais!')

 else:
    print ('Escaleno! todos diferentes!')

else:
   print('Não foi possivel fazer um triangulo! ')    