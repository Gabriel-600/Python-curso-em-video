velo = float(input('Digite a velocidade do carro: '))
exe = velo - 80
multa = exe * 7

if velo > 80:
    print ('Voce foi multado! ')
    print ('Sua multa é de R${:.2f}'.format (multa))

else:
    print ('Nao foi multado! ')