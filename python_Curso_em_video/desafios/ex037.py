num = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão:''')
print('[1] converter para BINARIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opcao = int(input('Digite sua opção! '))


if opcao == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)[2:]))

elif opcao == 2 :
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))

elif opcao == 3:
    print ('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))

else:
    print ('Opção invalida!! ')