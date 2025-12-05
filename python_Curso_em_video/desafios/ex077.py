print ('-'*50)
print(f'{"VOGAIS NAS PALAVRAS!":^50}')
print('-'*50)

palavras = ("APRENDER","PROGRAMAR","LINGUAGEM","PYTHON","CURSO","GRATIS","ESTUDAR","PRATICAR","TRABALHAR","MERCADO","PROGRAMAOR","FUTURO")

for item in palavras:
    print(f'\nNa palavra {item}, temos:', end=' ')
    for letra in item:
        if letra in "aeiouAEIOU":          #Se precisar poe com àâã éêê, etc.... 
            print(letra, end=' ')
            
print()
print('-'*50)
print('FIM!')