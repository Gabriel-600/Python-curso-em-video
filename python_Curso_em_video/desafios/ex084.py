lista = []
tempo = []
#cont = 0
maior = menor = 0
while True:
    tempo.append(str(input('Nome: ')))
    tempo.append(float(input('Peso: ')))
    if  len(lista) == 0:
        maior = menor = tempo[1]
    else:
        if tempo[1] > maior:
            maior = tempo[1]
        
        if tempo[1] < menor:
            menor = tempo[1]

    #cont += 1
    lista.append(tempo[:])
    tempo.clear()

    seguir = str(input('Quer continuar? [S/N]')) .strip() .upper()[0]
    while seguir not in 'SN':
        print('opçao invalida! ',end='')
        seguir = str(input('Quer continuar? [S/N]')) .strip() .upper()[0]
    if seguir == 'N':
        break       



print('-='*30)
print(f'Ao todo você cadastrou {len(lista)} pessoas!')
print(f'A mais pesada foi {maior}kg o peso de: ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')


print(f'\nA mais leve foi {menor}kg o peso de: ',end='')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'{[pessoa[0]]}', end='')