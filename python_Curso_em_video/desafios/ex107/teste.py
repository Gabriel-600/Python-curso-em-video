import moedas

p = int(input('Digite o preço: R$'))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(p, 10)}')

