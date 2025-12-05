# SO ADICIONA SE NÃO ESTIVER NA LISTA!

numeros = []

while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso!')

    else:
        print('Valor duplicado!')

    escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    while escolha not in 'SN':
        print('Opção invalida! digite novamente: ',end='')
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]

    if escolha == 'N':
        break

maior = max(numeros)
menor = min(numeros)
numeros.sort()
print('-='*30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor foi {maior}!')
print(f'O menor valor foi {menor}!')