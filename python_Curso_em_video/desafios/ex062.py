primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão '))
termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} , '.format(termo) ,end='')
        termo += razao
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos mais? '))
print('Progressão finalizada com {} termos mostrados '.format(total))