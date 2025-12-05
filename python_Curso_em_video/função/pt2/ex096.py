def area(L, C):
    resultado = L * C
    print(f'A area de um terreno {L}x{C} é de {resultado}')


#Programa principal
largura = float(input('Largura (M): '))
comprimento = float(input('Comprimento (M): '))

area(largura, comprimento)