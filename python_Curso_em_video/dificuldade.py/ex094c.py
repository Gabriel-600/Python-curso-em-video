pessoa = {}
galera = []
media = mulher = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo: [M/F] ')) .strip() .upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F!')
    
    
    pessoa["idade"] = int(input('Idade: '))
    galera.append(pessoa.copy())
    media += pessoa['idade']
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip() .upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! digite apenas S ou N!')
    if continuar == 'N':
        break

print('-='*30)
media = media / len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas!')
print(f'A media de idades foi {media}')
print('As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{pessoa["nome"]}')
print('Lista de pessoas acima da media de idades: ', end='')
for p in galera:
    if p["idade"] >= media:
        for k, v in p.items():
            print(f'{k} = {v} ')
        print()

print('<< ENCERRANDO >>') 




'''pessoa = {}
galera = []
media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F!')
    
    pessoa["idade"] = int(input('Idade: '))
    galera.append(pessoa.copy())
    media += pessoa['idade']
    
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! digite apenas S ou N!')
    if continuar == 'N':
        break

print('-=' * 30)
media = media / len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas!')
print(f'A média de idades foi {media:.2f}')

# --- Mulheres cadastradas ---
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()  # quebra de linha

# --- Pessoas acima da média ---
print('Lista de pessoas acima da média de idades:')
for p in galera:
    if p["idade"] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()  # quebra de linha por pessoa

print('<< ENCERRANDO >>')
'''