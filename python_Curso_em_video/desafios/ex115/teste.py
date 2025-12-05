from time import sleep
from bib.interfaca import *
from bib.arquivo import *

#Criar arquivo

arq = 'cursoemvideo.txt'
if not ArquivoExiste(arq):
    CriarArquivo(arq)

if ArquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        # Opção de listar conteudo de um arquivo.
        LerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        Cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... ate logo!')
        break
    else:
        # Digitou algo errado no menu.
        cabeçalho('\033[31mERRO! Resposta invalida!\033[m')
    sleep(1)

    