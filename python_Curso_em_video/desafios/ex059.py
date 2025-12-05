num1 = int(input('Digite um Numero: '))
num2 = int(input('Digite o segundo Numero: '))
escolha = 0



while escolha != 5:
    print ("""     
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa""")


    escolha = int(input('Oque deseja fazer? \n'))

    if escolha == 1:
        print('A resposta é',num1 + num2)
    elif escolha == 2:
        print('A resposta é ',num1 * num2)
    elif escolha == 3:
       if num1 > num2:
          print ('{} é maior que {}'.format(num1, num2))
       else:
          print ('{} é maior que {}'.format(num2, num1))
    elif escolha == 4:
        num1 = int(input('Digite Outro Numero: '))
        num2 = int(input('Digite mais um Numero: '))
    elif escolha == 5:
        print('Fim!')

    else:
        print('Escolha invalidada tente novamente!')
