from random import randint
from operator import itemgetter

# Passo 1: perguntar quantos jogadores
quantidade = int(input("Quantos jogadores vão jogar? "))
jogadores = {}

# Passo 2: cadastrar nomes e inicializar pontuação
for c in range(1, quantidade+1):
    nome = input(f"Nome do {c}º jogador: ")
    jogadores[nome] = randint(0, 100)  # sorteia a pontuação automaticamente

# Passo 3: mostrar pontuação de cada jogador
print("\n=== RESULTADO DA PARTIDA ===")
for nome, pontos in jogadores.items():
    print(f"{nome} marcou {pontos} pontos!")

# Passo 4: gerar ranking usando itemgetter
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Passo 5: mostrar ranking final
print("\n=== RANKING FINAL ===")
for i, v in enumerate(rank):
    print(f"{i+1}º lugar: {v[0]} com {v[1]} pontos")


'''from random import randint

jogadores = []  # lista que vai guardar todos os jogadores

for c in range(3):  # por exemplo, 3 jogadores
    jogador = {}  # dicionário para um jogador
    jogador['nome'] = input(f'Nome do {c+1}º jogador: ')
    jogador['pontos'] = randint(0, 100)  # sorteia a pontuação
    jogadores.append(jogador)  # adiciona o dicionário na lista

# mostrar resultados
for j in jogadores:
    print(f"{j['nome']} marcou {j['pontos']} pontos!")
'''