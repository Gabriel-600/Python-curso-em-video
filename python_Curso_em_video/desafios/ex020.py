import random

n1 = input ('PRIMEIRO ALUNO ')
n2 = input ('SEGUNDO ALUNO ')
n3 = input ('TERCEIRO ALUNO ')
n4 = input ('QUARTO ALUNO ')
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)

print ('a ordem foi {}'.format (ordem))