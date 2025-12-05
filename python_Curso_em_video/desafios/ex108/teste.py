import moedas

p = int(input('Digite o preço: R$'))
print(f'A metade de {moedas.formas(p)} é {moedas.formas(moedas.metade(p))}') # type: ignore
print(f'O dobro de {moedas.formas(p)} é {moedas.formas(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.formas(moedas.aumentar(p, 10))}') # type: ignore
print(f'Diminuindo 10%, temos {moedas.formas(moedas.diminuir(p, 10))}') # type: ignore

