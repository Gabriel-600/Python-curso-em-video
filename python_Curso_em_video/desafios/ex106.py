# Paleta de cores ANSI
c = (
    '\033[m',        # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m'     # 6 - branco invertido
)

def ajuda(com):
    titulo(f'Acessando manaul do comando \'{com}\'',4)
    print(c[4], end='')  # azul
    help(com)
    print(c[0], end='')  # volta pro normal

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')




# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 2)
