# Programa que lê um valor em metros e converte para cm e mm

metros = float(input("Digite o valor em metros: "))

centimetros = metros * 100   # 1 metro = 100 cm
milimetros = metros * 1000   # 1 metro = 1000 mm

print("O valor em metros: {} m".format(metros))
print("Convertido em centímetros: {} cm".format(centimetros))
print("Convertido em milímetros: {} mm".format(milimetros))
