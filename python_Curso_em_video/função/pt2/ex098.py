def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print('-='*30)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim +1, passo):
            print(c, end=' ')
        print('FIM!')
    if inicio > fim:
        for c in range(inicio, fim -1, -passo):
            print(c, end=' ')
        print('FIM!')

contador(1,10,1)

contador(10,0,2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)