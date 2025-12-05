def notas(*n, sit=False):
    alunos = {}
    alunos['Total'] = len(n)
    alunos['Maior'] = max(n)
    alunos['Menor'] = min(n)
    alunos['Media'] = sum(n) / len(n)
    if sit:
        if alunos['Media'] >= 7:
            alunos['Situação'] = 'BOA!'
        elif alunos['Media'] >=5:
            alunos['Situação'] = 'Razoavel!'
        else:
            alunos['Situação'] = 'Pessima!'


    return alunos
 




#Programa principal
dicionario = notas(4.5, 10, 6.7, 7.2, sit=True)
print(dicionario)