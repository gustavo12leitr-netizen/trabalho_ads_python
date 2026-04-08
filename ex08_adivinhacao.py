import random

# O computador escolhe o número
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("--- Jogo de Adivinhação (1 a 100) ---")

while not acertou:
    palpite = int(input("Qual o seu palpite? "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        acertou = True
    elif palpite < numero_secreto:
        print("Dica: O número é MAIOR.")
    else:
        print("Dica: O número é MENOR.")
