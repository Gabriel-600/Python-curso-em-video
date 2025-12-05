# OS MAIORES E MENORES VALOR DA LISTA!

list = []
for c in range (1,6):
    num = int(input(f'Digite o numero para a posição {c}: '))
    list.append(num)

print('-='*30)



maior = max(list)
menor = min(list)
print(f'Os valores digitados foram {list}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for pos, v in enumerate(list):
    if v == maior:
        print(pos)
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for pos, v in enumerate(list):
    if v == menor:
        print(pos)
print()



print('FIM!')