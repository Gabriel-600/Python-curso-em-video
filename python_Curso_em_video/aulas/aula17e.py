valor = []
for cont in range (0,5):
    valor.append(int(input('Digite um numero: ')))
print(valor)
for pos, v in enumerate(valor):
    print(f'O valor {v} esta localizado na posição {pos+1}')
print('FIM!')