import random
aluno1 = input ('PRIMEIRO ALUNO')
aluno2 = input ('SEGUNDO ALUNO')
aluno3 = input ('TERCEIRO ALUNO')
aluno4 = input ('QUARTO ALUNO')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)

print ('O escolhido foi {}'.format (escolhido))