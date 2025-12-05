teste = list()
teste.append('Gabriel')
teste.append(18)
galera = list()
galera.append(teste[:])         #[:] deixa eles "idependentes 1 do outro"
teste[0] = 'Maria'
teste[1] = 55
galera.append(teste[:])
print(galera)   