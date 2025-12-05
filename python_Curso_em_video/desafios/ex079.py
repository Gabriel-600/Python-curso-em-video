lista = []

while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('Valor adcionado com sucesso!')
    else:
        print('Valor duplicado...')

    seguir = ''
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N]')) .strip() .upper()[0]

    if seguir == 'N':
        break
 



print(f'Você digitou os valores {sorted(lista)}')





