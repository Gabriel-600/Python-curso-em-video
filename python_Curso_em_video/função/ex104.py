def leiaint(str):
    valor = 0
    ok = False
    while True:
        num = input(str)                                 #Tipo substitui o input que não usei no programa principal
        if num.isnumeric():                             #Se transforar em inteiro ok recebe True
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas numeros!\033[m')

        if ok:
            break
    return valor


#Programa principal
n = leiaint('Digite um numero: ')               #Digite um numero é o str da função
print(f'Você digitou o numero {n}') 