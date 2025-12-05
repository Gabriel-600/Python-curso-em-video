num =  sim = cont = soma = media = maior = menor =0
sim = 's'
while sim == 's':
    num = int(input('Digite um numero: '))
    soma +=num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
         
    sim = str(input('Quer continuar? [S/N] ')) .lower() .strip()[0]
  
media = soma / cont

print('Você Digitou {} numeros e a media foi {:.2f}\n'.format(cont, media))
print ('O maior valor foi {} e o menor foi {}'.format(maior, menor))