sal = float (input ('Qual o seu salario? R$'))
desc = sal + (sal * 15 / 100)

print ('Seu salario antigo era R${:.2f}, com os 15% agora seu salario é: {:.2f}'.format (sal, desc))