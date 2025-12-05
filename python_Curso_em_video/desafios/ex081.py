lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num) 
    
    resp = str(input('Quer continuar? [S/N] ')) .strip() .upper()[0]
    while resp not in 'SN':
        print('Resposta invalida! ',end='')
        resp = str(input('Quer continuar? [S/N] ')) .strip() .upper()[0]

    if resp == 'N':
        break

lista.sort(reverse=True)
   
print('-='*30)

print(f'Você digitou {len(lista)} elementos!')
print(f'Os valores em ordem decrescente são: {lista}!')
if 5 in lista:
    print('O valor 5 faz parte da lista! na posição: ', end='')
    for i , v in enumerate(lista):
        if v == 5:
            print(f'{i+1}', end='')
    print()
else:
    print('O valor 5 não faz parte da lista!')  
        