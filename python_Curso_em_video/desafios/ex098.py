def contagem1():
    num = 0
    print('Contagem de 1 ate 10 de 1 em 1: ')
    while num != 10:
        num +=1
        print(num, end=' ')
    print('FIM!')


def contagem2():
    print('Contagem de 10 ate 0 de 2 em 2: ')
    for c in range (10 ,-1 ,-2):
        print(c, end=' ')
    print('FIM!')

def contagem3(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if passo == 0:
        passo = 1  # evita erro (não pode ser 0)
    
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):  # contagem crescente
            print(c, end=' ')
    else:
        for c in range(inicio, fim - 1, -abs(passo)):  # contagem regressiva
            print(c, end=' ')
    
    print('FIM!')

print('-='*30)
contagem1()
print('-='*30)
contagem2()
print('-='*30)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem3(inicio, fim, passo)
print('-='*30)