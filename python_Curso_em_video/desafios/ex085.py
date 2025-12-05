valores = [[], []]
for c in range(1,8):
    num = int(input(f'Digite o {c} valor: '))

    if num % 2 == 0:
        valores[0].append(num)                              #num[0].append(valor) tb se os valores for num

    else:
        valores[1].append(num)
    
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares são {valores[0]}')
print(f'OS valores impares são {valores[1]}')