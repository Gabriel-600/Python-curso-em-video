def leiaint(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite apenas numeros inteiros validos!\033[m')
            continue
        except (KeyboardInterrupt):
            print('Saida forçada de dados!')
        else:
            return n 


def linha(tam=42):
    return '-'*tam


def menu(text):
    print(linha())
    print(text.center(42))
    print(linha())

def opções(lista):
    for i,v in enumerate(lista):
        print(f'{i+1} - {v}')
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


'''def leiaint(text):
    while True:
        try:
            n = int(input(text))
        except (TypeError,ValueError):
            print('ERRO! digite apenas numenos inteiros validos!')
            continue
        except KeyboardInterrupt:
            print('ERRO! Saida forçada de dados!')
            return 0
            break
        else:
            return n'''