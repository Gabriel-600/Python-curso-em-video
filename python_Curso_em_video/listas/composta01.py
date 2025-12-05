pesos = []
temp = []
while True:
    nome = str(input('Nome: '))
    temp.append(nome)
    peso = float(input('Peso: '))
    temp.append(peso)
    pesos.append(temp[:])
    temp.clear()
    esc = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    while esc not in 'SN':
        print('Escolha invalida! Digite novamente! ', end='')
        esc = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    if esc == 'N':
        break

maior = menor = pesos[0][1]
for p in pesos:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

print('-='*30)
print(f'Ao todo você cadastrou {len(pesos)} pessoas! ')
print(f'O maior peso foi de {maior}KG. peso de: ', end='')
for p in pesos:
    if p[1] == maior:
        print(p[0], end='')
print()
print(f'O menor peso foi de {menor}KG. peso de: ', end='')
for p in pesos:
    if p[1] == menor:
        print(p[0], end='')

'''maior = menor = pesos[0][1]
for p in pesos:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]
'''