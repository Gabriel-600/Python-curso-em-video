def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo <0:
        passo = -passo
    print('-='*30)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range (inicio, fim +1 ,passo):
            print(c, end=' ')
        print('FIM!')
    if inicio > fim:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ') 
        print('FIM!')  

contagem(1,10,1)

contagem(10,0,2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)