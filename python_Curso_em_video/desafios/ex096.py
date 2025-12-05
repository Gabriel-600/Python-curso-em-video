def area(larg,comp):
    s = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {s:.2f}m².')
    
    #programa principal
larg = float(input('LARGURA (M): '))
comp = float(input('COMPRIMENTO (M): '))

area(larg, comp)