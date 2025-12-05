def maior(*numeros):
    print('-='*30)
    maior = menor = cont = 0
    print('Analisando os valores passados...')
    for n in numeros:
        print(n, end=' ')
    print(f'foram informados {len(numeros)} numeros!')
    for n in numeros:

        if cont == 0:
            maior = n
            menor = n

        else:
            if n >= maior:
                maior = n
   
            if n <= menor:
                menor = n
        cont += 1

    print(f'O maior numero foi {maior} ')
    print(f'O menor numero foi {menor}')

maior(3,4,6,8)
maior(10,20,30,40)
maior()
maior(2,3)
