# VALOR 5 NA LISTA E DECRESCENTE!

numeros = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)

    go = str(input('Quer continuar? [S/N]: ')).strip() .upper()[0]
    while go not in 'SN':
        print('Escolha invalida! ',end='')
        go = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    if go == 'N':
        break

numeros.sort(reverse=True)
print('-='*30)

print(f'Foram digitados {len(numeros)}')
print(f'Os valores na ordem decrescente é {numeros}')
if 5 in numeros:
    print('O valor 5 esta na lista!')
else:
    print('O valor 5 não foi encontrado!')