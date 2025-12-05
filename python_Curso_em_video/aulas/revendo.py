valores = []

while True:
    num = int(input('Digite um numero: '))

    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor ja esta na lista!')
    

    escolha = str(input('Quer continuar [S/N]: ')) .strip() .upper()[0]
    while escolha not in 'SN':
        print('Digite novamente! ', end='')
        escolha = str(input('Quer continuar? [S/N]: ')).strip() .upper()[0]

    if escolha == 'N':
        break

print('-='*30)
# ou valores.sort() pra por em ordem!
print(f'Você digitou os valores {sorted(valores)}')