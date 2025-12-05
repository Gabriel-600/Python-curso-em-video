from random import randint
jogador=0
jogada = 0
cont = 0
print ('-='*20)
print('Vamos jogar par ou impar! ' )
print ('-='*20)



while True:
    jogador = int(input('Digite um valor [0 a 10] '))
    escolha = str(input('Par ou impar [P/I] ')) .strip() .upper()
    pc = randint(0, 11)
    jogada = pc + jogador
    while escolha not in 'PI':
        escolha = str(input('Escolha invalida eschola entre [P/I]')) .strip() .upper()

# par e impar

    if jogada % 2 == 0:
         resultado = 'P'
         print('PAR!')
    
    else:
        resultado ='I'
        print('IMPAR!') 

#resultado se venceu ou n

    if escolha == resultado:
        print(f'Você venceu! Você jogou {jogador} e o computador jogou {pc}')
        print('Jogue novamente!')
        
    else:
        print(f'Você perdeu! Você jogou {jogador} e o computador jogou {pc}')
        break
        
    cont += 1

print(f'Fim Você ganhou {cont} vezez!')






















