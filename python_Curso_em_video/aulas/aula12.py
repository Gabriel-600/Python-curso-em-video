nome = str(input('Qual o seu nome? ')).lower() .strip()
if nome == 'Gabriel':
    print('Que nome lindoooouuu')

elif nome == 'Jhu' or nome == 'papa' or nome == 'marcio':
    print ('Nome divertido!')

else:
    print ('Nome ridiculo!')

print ('Tenha um bom dia {}!'.format(nome))