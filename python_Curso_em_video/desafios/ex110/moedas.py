def aumentar(preço=0, taxa=0 ,format=False):
    res = preço + (preço * taxa/100)
    return res if format is False else formas(res) # type: ignore # 1.10 pra aumentar 10% 1.50 50 % etc...       round arredonda

def diminuir(preço=0, taxa=0 ,format=False):
    res = preço - (preço * taxa/100)
    return res if format is False else formas(res) # type: ignore # 0.90 diminui 10%   0.50 diminui 50# etc... 

def dobro(preço=0, format=False):
    res = preço * 2
    return res if format is False else formas(res)    # type: ignore

def metade(preço=0, format=False):
   res = preço / 2   
   return res if format is False else formas(res)    # type: ignore


def formas(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*20)
    print('RESUMO DO VALOR'.center(20))
    print('-'*20)   
    print(f'Preço analisado: \t{formas(preco)}    ') 
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa,True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)


           