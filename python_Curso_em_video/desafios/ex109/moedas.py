def aumentar(preço=0, taxa=0 ,format=False):
    res = preço + (preço * taxa/100)
    return res if format is False else formas(res) # type: ignore

def diminuir(preço=0, taxa=0 ,format=False):
    res = preço - (preço * taxa/100)
    return res if format is False else formas(res) # type: ignore

def dobro(preço=0, format=False):
    res = preço * 2
    return res if format is False else formas(res)    # type: ignore

def metade(preço=0, format=False):
   res = preço / 2   
   return res if format is False else formas(res)    # type: ignore


def formas(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')



# 0.90 diminui 10%   0.50 diminui 50# etc...             # 1.10 pra aumentar 10% 1.50 50 % etc...       round arredonda