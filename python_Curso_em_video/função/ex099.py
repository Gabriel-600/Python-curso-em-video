def maior(*numeros):
    print('-='*30)
    print('Analisando os numeros recebidos...\n')
    cont = maior = menor = 0
    for n in numeros:
        if cont == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

        cont += 1
    print(f'Foram passados {cont} valores.')
    print(f'O maior valor foi {maior}! e o menor foi {menor}\n')
    print('-='*30)





maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(9)

numeros = []
while True:
    num = int(input('Digite numeros (999 pra parar!): '))
    if num == 999:
        break
    numeros.append(num)

maior(*numeros)
