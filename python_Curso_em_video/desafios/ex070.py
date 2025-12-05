print('-'*20)
print('Loja Mercenarios!')
print('-'*20)

total =  mil = cont = menor = 0
nomeprod = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont +=1
    opcao = ''
    total += preco

    if preco > 1000:
        mil += 1

    if cont == 1:
        menor = preco
        nomeprod = produto
    else:
        if preco < menor:
            menor = preco
            nomeprod = produto

    while opcao not in ('S', 'N'):
        opcao = str(input('Quer continuar [S/N]: ')) .strip() .upper()[0]
    if opcao == 'N':
        break

print('Encerrando....')      
print(f'O total deu R${total}')
print(f' produtos deram valor acima de 1000: {mil} ')
print(f'O produto mais barato foi: {nomeprod} de {menor}')