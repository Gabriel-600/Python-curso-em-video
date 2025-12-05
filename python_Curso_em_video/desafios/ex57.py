sexo = str(input('Digite seu sexo M/F: ')) .strip() .upper()[0]
while sexo != 'M' and sexo != 'F':
    print ('Mensagem invalida!')
    sexo = str(input('Digite novamente:')) .strip() .upper()
    
if sexo == 'M':
    print('Você é do sexo Masculino! ')
elif sexo == 'F':
    print('Você é do sexo Feminino')
