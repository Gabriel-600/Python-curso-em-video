galera = []
pessoa = {}
soma = media = 0
while True: 
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()
        if pessoa['sexo'] in ['M', 'F']:
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:    
        resp = str(input('Quer continuar? [S/N]: ')) .strip() .upper()
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break


print('-='*30)
print(f'A) Foram cadastradas {len(galera)} pessoas! ')
media = soma / len(galera)
print(f'B) A media das idades é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ',end=',')
for p in galera:
   if p['sexo'] == 'F':
    print(f'{p["nome"]}',end=' ')
print()
print(f'D) pessoas com idade acima da media: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('      ')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ',end='')
        print()
print('-=')
print('<< ENCERRADO >>')