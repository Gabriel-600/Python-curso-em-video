import moedas

p = int(input('Digite o preço: R$'))
print(f'A metade de {moedas.formas(p)} é {(moedas.metade(p,True))}') # type: ignore
print(f'O dobro de {moedas.formas(p)} é {(moedas.dobro(p, True))}') # type: ignore
print(f'Aumentando 10%, temos {(moedas.aumentar(p, 10, True))}') # type: ignore
print(f'Diminuindo 10%, temos {(moedas.diminuir(p, 10, True))}') # type: ignore

