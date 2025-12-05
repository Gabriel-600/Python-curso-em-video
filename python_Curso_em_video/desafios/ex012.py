preco = float (input('Qual o valor? '))
dec = preco - ( preco * 5 / 100)
print ('O produto que custava R${:.2f}, com desconto de 5% vai custar R${:.2f}'.format(preco, dec))