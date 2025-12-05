galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')) .strip() .upper()[0]         
        if pessoa['sexo'] in ['M','F']:
            break
        print('Erro Responda apenas com M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
        if escolha in ['S','N']:
            break
        print('Erro! Responda apenas com S ou N')
    if escolha == 'N':
        break

print('-='*30)

print(f'Foram cadastradas: {len(galera)} pessoas!')
media = soma / len(galera)
print(f'A media das idades é de {media:5.2f}')
cont = 0
print(f'As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] == 'F':
        cont +=1
        print(f'{p['nome']}, ',end='')
print(f'Ao todo foram {cont} mulheres! ')

print('As pessoas acima da media de idade foram: ',end=' ')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}!', end='')






''' # mulheres
mulheres = [p['nome'] for p in galera if p['sexo'] == 'F']
print(f"As mulheres cadastradas foram: {', '.join(mulheres)} (total: {len(mulheres)})")

# pessoas acima da média
acima_media = [p['nome'] for p in galera if p['idade'] > media]
print(f"As pessoas acima da média de idade foram: {', '.join(acima_media)}")'''