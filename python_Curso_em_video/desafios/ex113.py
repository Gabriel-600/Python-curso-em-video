def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor leia um numero inteiro valido!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuario!')
            return 0
            break
        else:
            return n 

def leiafloat(msg):
    while True:
        try:
            oi = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um valor inteiro valido!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuario!')
            return 0 
            break
        else:
            return oi


inteiro = leiaint('Digite um valor inteiro: ')
real = leiafloat('Digite um valor real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real {real}')



'''def leiafloat(msg):
    while True:
        try:
            s = input(msg)
            if "." not in s:   # <-- obriga ter ponto decimal
                raise ValueError

            n = float(s)

        except (ValueError, TypeError):
            print('ERRO! Digite um número REAL (com ponto). Ex: 3.5')
            continue
        except KeyboardInterrupt:
            print('\nEntrada interrompida pelo usuário!')
            return 0
        else:
            return n
'''