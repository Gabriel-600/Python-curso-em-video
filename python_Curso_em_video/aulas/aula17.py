lanches = ["Pizza","Hamburguer","Suco","Pudim"]
lanches[3] = 'picole'
lanches.append('Uva')
lanches.insert(0,'Cachorro-Quente')
print(lanches)
lanches.pop(1)
if 'Pizza' in lanches:
    lanches.remove("Pizza")

print(lanches)

'''for comida in lanches:
    print(comida,end=' ')'''
    