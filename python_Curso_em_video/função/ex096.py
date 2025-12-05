def area():
    larg = float(input('Largura (M): '))
    comp = float(input('Compriemnto (M): '))
    resultado = larg * comp
    print(f'A área de um terreno {larg}x{comp} é {resultado}m².')

print('Controles de Terrenos')
print('-'*20)

area()