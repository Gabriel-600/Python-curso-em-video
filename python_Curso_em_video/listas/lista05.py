# PAR E IMPAR!

numeros = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    # Numeros par
    if num % 2 ==0:
        par.append(num)
    # Numeros impar    
    else:
        impar.append(num)

    escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    while escolha not in 'SN':
        print('Escolha invalida! ', end='')
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0] 
    if escolha == 'N':
        break

print('-='*30)
print(f'Os valores digitados foram {numeros}! ')
print(f'Os valores pares digitados foram {par}!')
print(f'Os valor impares digitados foram {impar}!')