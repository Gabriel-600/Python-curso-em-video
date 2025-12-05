def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas numeros!\033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
