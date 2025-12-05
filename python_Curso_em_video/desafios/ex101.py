#from datetime import date

'''def voto(idade):
    if idade >=18:
        return f'Com {idade} anos: Voto Obrigatorio!'
    elif idade >=70:
        return f'Com {idade} anos: Voto Opicional!'
    else:
        return f'Com {idade} anos: Não vota!'

ano_nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano_nasc

print(voto(idade))
'''




#guanabara 

def voto(ano):
    '''Calcula a idade e vê a votação é obrigatoria opcional ou nao vota'''
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com idade {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'
    
nasc = int(input('Em que ano você nasceu: '))

print(voto(nasc))


help(voto)