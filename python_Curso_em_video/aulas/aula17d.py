num = []
num.append(2)
num.append(9)
num.append(2.5)
num.insert(0,20)
print(num)

for pos,valor in enumerate(num):
    print(f'O numero {valor} esta na posição numero: {pos+1}')

print('FIM!')