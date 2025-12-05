Tabela = (
    "Flamengo",
    "Cruzeiro",
    "Palmeiras",
    "Mirassol",
    "Botafogo",
    "Bahia",
    "São Paulo",
    "Fluminense",
    "Red Bull Bragantino",
    "Corinthians",
    "Grêmio",
    "Ceará",
    "Vasco",
    "Internacional",
    "Santos",
    "Atlético-MG",
    "Vitória",
    "Juventude",
    "Fortaleza",
    "Sport"
)


print(f'Tabela Brasileirão: {Tabela}\n')

print('=-'*70)

print(f'Os cinco primeiros são {Tabela[:5]}\n') 

print('=-'*70)

print(f'Zona de rebaixamento: {Tabela[-4:]}\n')

print('-='*70)

print(f'Times em ordem alfabetica: {sorted(Tabela)}')

print('-='*70)

print('O flamengo esta na posição:',Tabela.index("Flamengo")+1)
    