galera = list()
dado = list()

for c in range (0,3):
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()    
print(galera)

for pessoa in galera:
    if pessoa[1] >=18:
        print(f'{pessoa[0]} é maior de idade! ')
    else:
        print(f'{pessoa[0]} é menor de idade! ')