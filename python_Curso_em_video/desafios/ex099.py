from time import sleep


def maior(*num):
     print('-='*30)
     print('Analisando os valores informados...')
     
     cont = maior = menor = 0
     for valor in num:
          sleep(0.2)
          print(valor, end=' ')
          if cont == 0:
               maior = valor
               menor = valor
          else:
            if valor > maior:
                maior = valor
            else:
                if valor < menor:
                    menor = valor
          cont += 1
     print(f'foram informados {cont} valores')
     print(f'O maior valor é {maior} e o menor {menor}')

                    


 
maior(2,9,4,5,7,1,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
