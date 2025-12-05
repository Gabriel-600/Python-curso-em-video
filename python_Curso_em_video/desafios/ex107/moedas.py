def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res

def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço=0):
    return preço * 2

def metade(preço=0):
    return preço / 2





# 0.90 diminui 10%   0.50 diminui 50# etc...             # 1.10 pra aumentar 10% 1.50 50 % etc...       round arredonda