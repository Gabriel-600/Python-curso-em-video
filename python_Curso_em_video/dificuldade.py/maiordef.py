from time import sleep


def maior(*numeros):
    print('-='*30)
    print('Analisando...\n')
    cont = maior = menor = 0
    for valor in numeros:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        cont +=1
    print(f'foram informados {cont} numeros')
    print(f'O maior numero foi {maior} e o menor foi o {menor}')

maior(3,8,10,22,0,2)
maior(2,2,1,3,4,6,)
maior(1,2,3,4,5,6,7,8,9,10)
maior(5,10)