def notas(*notas, sit=False):
    """Dicionario com informçoes das notas passadas

    Args:
        sit (bool, optional): Valor opcional indicando se deve ou não mostra a situação Defaults to False.

    Returns:
        Dicionario com informações das notas passadas
    """
    r = {}
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = (sum(notas)) / len(notas)

    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >=5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim '

    return r 


#Programa principal
resp = notas(5.5, 2.5, 1.5, 6, 2, sit=True)
print(resp)
