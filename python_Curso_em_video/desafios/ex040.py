n1 = float(input('Digite sua nota: '))
n2 = float (input('Digite sua outra nota: '))
result = (n1 + n2) /2

if result <5.0:
    print('REPROVADO! Sua media foi {}'.format(result))

elif result < 7:
    print('RECUPERAÇÃO Sua media foi {}'.format(result)) 

else:
    print ('APROVADO! Sua media foi {}'.format(result))