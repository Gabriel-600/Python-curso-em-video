import random

print("=== Pedra, Papel ou Tesoura ===")

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Jogador escolhe
jogador = input("Escolha pedra, papel ou tesoura: ").lower()

# Computador escolhe
computador = random.choice(opcoes)

print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

# Regras do jogo
if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") \
   or (jogador == "papel" and computador == "pedra") \
   or (jogador == "tesoura" and computador == "papel"):
    print("Você venceu! 🎉")
elif jogador in opcoes:
    print("Você perdeu! 😢")
else:
    print("Jogada inválida!")
