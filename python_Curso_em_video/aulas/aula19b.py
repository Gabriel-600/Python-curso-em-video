filmes = {}
filmes = {'titulo':'Star wars', 'ano': '1977','diretor': 'George lucas'}
print(filmes.items())

for k, v in filmes.items():
    print(f'O {k} é {v}')