valor = []
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valor[-1]:
        valor.append(num)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos <len(valor):
            if num <= valor[pos]:
                valor.insert(pos,num)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos +=1

print('-='*30)
print(f'Os valores digitados em ordem foram {valor}!') 