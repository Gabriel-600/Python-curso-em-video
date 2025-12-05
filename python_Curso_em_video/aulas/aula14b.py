num = 1
impar = 0 
par = 0 

while num != 0:
  num = int(input('Digite Um numero! '))
  if num != 0:
    if num % 2 == 0:
            par += 1
    elif num % 2 ==1:
        impar += 1
print('Foram {} Numeros pares, e {} Numeros impares!'.format(par, impar))