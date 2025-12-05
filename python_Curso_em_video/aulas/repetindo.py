lista = []
temp = []

while True:
    temp.append ((input('Digite o nome: ')))
    temp.append (float(input('Digite o peso: ')))
    lista.append(temp[:])
    temp.clear()
    escolha = str(input('Quer continuar? [S/N]: ')) .upper() .strip()
    while escolha not in 'SN':
        print('Opção invalida! ', end=' ')
        escolha = str(input('Quer continuar? [S/N]: ')) .upper() .strip()

    if escolha == "N":
        break

maior = menor = lista[0][1]

for pessoa in lista:
    if pessoa[1] > maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]




print('-='*30)
print(f'Ao todo foram cadastradas {len(lista)} pessoas!')
print (f'O maior peso foi kg{maior} esse peso foi do: ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(pessoa[0])
print(f'O menor peso foi de kg{menor} esse peso foi do: ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(pessoa[0])
