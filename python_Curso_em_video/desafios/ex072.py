numeros = ('zero','Um','Dois','Três','Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove',
           'Dez','Onze','Doze','Treze', 'Quatorze','Quinze','Dezesete','Dezoito',
           'Dezenove','Vinte')  
#Verificar se o num é valido e mostra ele em tupla
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    
    while num < 0 or num > 20:
        num = int(input('Número inválido! Digite novamente entre 0 e 20: '))
    
    print(f'Você digitou {numeros[num]}!')
    
   #Quer continuar? 
 
    escolha = ''
    while escolha not in ('S', 'N'):
        escolha = input('Quer continuar? [S/N] ').strip().upper()
        if escolha not in ('S', 'N'):
            print('Opção inválida! Digite apenas S ou N.')
    
    if escolha == 'N':
        break

print('Fim!')


'''
num = int(input("Digite um número entre 0 e 20: "))

while num < 0 or num > 20: 
    num = int(input("Tente novamente! Digite um número entre 0 e 20: "))

print("Você digitou:", numeros[num])'''
