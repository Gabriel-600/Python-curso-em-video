pessoa = {'Nome':'Gabriel', 'idade':'18','Sexo':'M'}
del pessoa['Sexo']     #deleta um item do dicionario
pessoa['peso'] = 65    # adiciona tipo um append
for k, v in pessoa.items():
    print(f'{k} = {v}')