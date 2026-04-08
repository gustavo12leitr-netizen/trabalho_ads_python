# Exercício 5: Tabuada Dinâmica
num = int(input("Deseja ver a tabuada de qual número? "))
fim = int(input("Até qual valor deseja calcular? (ex: 10, 20): "))

print(f"\n--- Tabuada do {num} (1 até {fim}) ---")

# O range(1, fim + 1) garante que o loop vá do 1 até o número escolhido
for i in range(1, fim + 1):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
