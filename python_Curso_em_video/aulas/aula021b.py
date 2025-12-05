def teste(b):
    global a 
    a = 8
    b += 5
    print(f'Dentro {a}')

a = 5
teste(a)
print(f'fora {a}')