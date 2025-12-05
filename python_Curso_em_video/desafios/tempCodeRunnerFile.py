def contagem3(inicio, fim, passo):
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('FIM!')