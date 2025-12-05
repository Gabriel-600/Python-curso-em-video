id = int(input('Digite a idade: '))

if id <=9:
    print ('Mirim!, Você tem {} anos.'.format(id))

elif  id  <=14 :
    print('Infantil!, Você tem {} anos!'.format(id))

elif id <= 19:
    print('Junior!, Você tem {} anos!'.format(id))

elif id ==20:
    print('Sênior!, Você tem {} anos!'.format(id))    

else:
    print ('MASTER!, Você tem {} anos.'.format(id))