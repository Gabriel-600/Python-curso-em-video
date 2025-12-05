pesos = []
temp = []
maior = menor = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    temp.append(nome)
    temp.append(peso)
    pesos.append(temp[:])  # copia o conteúdo de temp para a lista pesos
    temp.clear()  # limpa a lista temporária para o próximo cadastro

    if len(pesos) == 1:
        maior = menor = peso  # primeiro cadastro define ambos
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida! ', end='')
        escolha = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pesos)} pessoas.')
print(f'O maior peso foi {maior} kg. Peso de ', end='')
for pessoa in pesos:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso foi {menor} kg. Peso de ', end='')
for pessoa in pesos:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')
print()


'''pesos = []
temp = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    temp.append(nome)
    temp.append(peso) 
    pesos.append(temp[:])
    if len(pesos) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    
   
    temp.clear()
    escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    while escolha not in 'SN':
        print('Opção invalida! ', end='')
        escolha = input('Quer continuar? [S/N]: ') .strip() .upper()[0]
    if escolha == 'N':
        break


print('-='*30)
print(f'Ao todo você cadastrou {len(pesos)} pessoas!')
print(f'O maior peso foi {maior} do: ', end='')
for pessoa in pesos:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso foi {menor} do: ', end='')
for pessoa in pesos:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end='')
print()




'''