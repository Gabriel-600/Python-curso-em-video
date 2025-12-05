from time import sleep
from biblioteca.interfac import *


while True:
    menu('MENU PRINCIPAL')
    resp = opções(['Ver pessoas cadastradas','Cadastrar novas pessoas', 'Sair do sistema'])

    if resp == 1:
        menu('Pessoas cadastradas')
    elif resp == 2:
        menu('Cadastrar nova pessoa')
    elif resp == 3:
        menu('Saindo...')
        break
    else:
        print('ERRO! Escolha uma opção valida!')
    