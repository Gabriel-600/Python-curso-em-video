print('-'*25)
print('Cadastre uma pessoa!')
print('-'*25)

homem = anos = mulher20 = 0

while True:
    idade = int(input('Idade: '))

    # Sexo
    sexo = ''
    while sexo not in ('M', 'F'):
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    print('-'*25)

    # Contagens
    if idade >= 18:
        anos += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    # quer continuar
    resposta = ''
    while resposta not in ('S', 'N'):
        resposta = input('Quer continuar? [S/N]: ').strip().upper()
    print('-'*25)

    if resposta == 'N':
        break

print('Analisando...')
print(f'Total de Pessoas com mais de 18 anos: {anos}')
print(f'Ao todo tem {homem} homens cadastrados!')
print(f'E tem {mulher20} mulher(es) com menos de 20 anos!')













