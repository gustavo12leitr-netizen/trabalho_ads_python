# Exercício 6: Contador de Vogais
frase = input("Digite uma frase: ").lower() # .lower() converte tudo para minúsculo
vogais = "aeiou"

# Dicionário para o Extra (contar separadamente)
contagem = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
total = 0

for letra in frase:
    if letra in vogais:
        contagem[letra] += 1
        total += 1

print(f"\nTotal de vogais encontradas: {total}")
print("Detalhamento:")
for v, qtd in contagem.items():
    print(f"Vogal '{v}': {qtd}")
